'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bug-report: keraymondyan69gmail.com
'''

import glob
from typing import List, Any, Dict

import yaml

import tools.utils as utils
from basic_handler import BasicHandler


class Handler(BasicHandler):
    """
    _task_payload: This is a dict. Its constitute is as:
    { <payload_file_name>: <[resource_url-01], [resource_url-02],...> }
    e.g.
    {
        "pushImage_payload_1572414199.yaml": [
        "harbor.sunvalley.com.cn/library/centos:7",
        "harbor.sunvalley.com.cn/library/centos:8"
        ]
    }
    """
    _task_payloads: Dict[str, str]

    def __init__(self, payload):
        super(Handler, self).__init__(payload)
        self._task_payloads = {}

    def handle(self, *payload):
        """
        :param payload: request's payload.
        :return: script execution result.
        1. Receive the payload from request.
        2. Serialize the payload to disk. In case of this script failed executed. I'll write a daemon program to scan
        if any serialized file exist, if yes, re-run this script.
        3. Do the logic.
        """
        # TODO: load token from file and compare it with the token from request
        pass

        if self.event_type == 'pushImage':
            # First, load serialized payloads from disk.
            payload_iter = glob.iglob('{0}_{1}_*.{2}'.format(self.event_type, 'payload', 'yaml'))
            # task_payload_tuple looks like: ('pushImage_payload_1572414199.yaml':
            # 'harbor.sunvalley.com.cn/library/centos:7')
            resource_urls = [resource['resource_url'] for resource in self.event_data['resources']]
            # TODO: First, find serialized files, if exist, append task to _task_payload dict.
            for file in payload_iter:
                resources = yaml.load(open(file, 'r'), Loader=yaml.FullLoader)['event_data']['resources']
                resource_urls.append([resource['resource_url'] for resource in resources])
                # Unique the resource_urls.
                unique_resource_urls: List[str] = utils.unique(resource_urls)
                self._task_payloads[file] = unique_resource_urls
            # TODO: Serialize the payload first, in case of this script failed.
            # The file looks like 'pushImage_payload_1572414199.yaml'.
            stream = open('{0}_{1}_{2}_{3}'.format(self.event_type, 'payload', self.occur_at, '.yaml'), 'w')
            yaml.dump(self.payload, stream)

            result = []
            for resource in self._task_payloads:
                # print(resource['resource_url'])
                # TODO: re-tag the resource, and push to defined registries. e.g. Aliyun registry, AWS registry.
                cp = utils.OSCommand('ls -lh ./file_not_exit'.split()).run()
                if cp.stderr:
                    result.append(cp.stderr)
                elif cp.stdout:
                    result += cp.stdout + resource['resource_url']
            return result

# if __name__ == '__main__':
#     print('push_image_handler.py')
