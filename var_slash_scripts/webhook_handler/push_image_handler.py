#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bug-report: keraymondyan69gmail.com
import glob
from typing import List, Any

import yaml

import utils
from basic_handler import BasicHandler
from tools.utils import OSCommand


class Handler(BasicHandler):

    def __init__(self, payload, task_payloads):
        super(Handler, self).__init__(payload)
        assert isinstance(task_payloads, list)
        self.task_payloads = task_payloads

    def handle(self, *payload):
        """
        :param payload: request's payload.
        :return: script execution result.
        1. Receive the payload from request.
        2. Serialize the payload to disk. In case of this script failed executed. I'll write a daemon program to scan
        if any serialized file exist, if yes, re-run this script.
        3. Do the logic.
        """
        if self.event_type == 'pushImage':
            # First, load serialized payloads from disk.
            payload_iter = glob.iglob('{0}_{1}_*.{2}'.format(self.event_type, 'payload', 'yaml'))
            # task_payload_tuple looks like: ('pushImage_payload_1572414199.yaml':
            # 'harbor.sunvalley.com.cn/library/centos:7')

            for file in payload_iter:
                resources = yaml.load(open(file, 'r'), Loader=yaml.FullLoader)['event_data']['resources']
                resource_urls = [resource['resource_url'] for resource in resources]
                # Unique the resource_urls.
                unique_resource_urls: List[Any] = utils.unique(resource_urls)
                self.task_payloads[file] = unique_resource_urls
            # TODO: Serialize the payload first, in case of this script failed.
            # The file looks like 'pushImage_payload_1572414199.yaml'.
            stream = open('{0}_{1}_{2}_{3}'.format(self.event_type, 'payload', self.occur_at, '.yaml'), 'w')
            yaml.dump(self.payload, stream)
            resources = self.event_data['resources']
            result = []
            for resource in resources:
                # print(resource['resource_url'])
                # TODO: re-tag the resource, and push to defined registries. e.g. Aliyun registry, AWS registry.
                p = OSCommand('command-not-exist').run()
                if p.stderr:
                    result.append(p.stderr)

                if p.stdout:
                    result += p.stdout + resource['resource_url']
            return result

# if __name__ == '__main__':
#     print('push_image_handler.py')
