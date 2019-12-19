#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bug-report: keraymondyan69gmail.com
import utils

if __name__ == '__main__':
    # payload_json = """
    # {
    #   "type": "pushImage",
    #   "occur_at": 1572414199,
    #   "event_data": {
    #     "resources": [
    #       {
    #         "digest": "sha256:a36b9e68613d07eec4ef553da84d0012a5ca5ae4a830cf825bb68b929475c869",
    #         "tag": "7",
    #         "resource_url": "harbor.sunvalley.com.cn/library/centos:7"
    #       }
    #     ],
    #     "repository": {
    #       "date_created": 1572414199,
    #       "name": "centos",
    #       "namespace": "library",
    #       "repo_full_name": "library/centos",
    #       "repo_type": "public"
    #     }
    #   },
    #   "operator": "robot$library-robot"
    # }
    # """
    # payload = json.loads(payload_json)
    # stream = open('{0}_{1}_{2}.{3}'.format('pushImage', 'payload', '1573109368', 'yaml', 'w')
    # print('{0}_{1}_{2}.{3}'.format('pushImage', 'payload', '1572414199', 'yaml'))
    # yaml.dump(payload, stream)
    '''
    event_type = 'pushImage'
    payload_iter = glob.iglob('{0}_{1}_*{2}'.format(event_type, 'payload', 'yaml'))
    task_payloads = {}

    for file in payload_iter:
        resources = yaml.load(open(file, 'r'), Loader=yaml.FullLoader)['event_data']['resources']
        resource_urls = [resource['resource_url'] for resource in resources]
        # Unique the resource_urls.
        unique_resource_urls = utils.unique(resource_urls)
        task_payloads[file] = unique_resource_urls
    for task in task_payloads:
        print(task, '\t', task_payloads[task])
    '''


    command = 'ls -lh ./file_not_exist'.split(' ')
    print(command)
    cp = utils.OSCommand(command).run()
    # print(type(cp))
    # print(dir(cp))
    print(vars(cp))
    result = []
    if cp.stderr:
        result.append(cp.stderr)
    elif cp.stdout:
        result += cp.stdout + resource['resource_url']
