#!/usr/bin/env python

import argparse
import importlib
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Harbor webhook endpoint handling script."
    )
    # parser.add_argument("--json-string", dest="payload_json",
    #                     help="Just pass the json of request's body to me.",
    #                     required=True, type=str)
    parser.add_argument('payload', help='Just pass the entire JSON payload to me.', type=str)
    # none = None
    payload_json = """
{
  "type": "pushImage",
  "occur_at": 1572414199,
  "event_data": {
    "resources": [
      {
        "digest": "sha256:a36b9e68613d07eec4ef553da84d0012a5ca5ae4a830cf825bb68b929475c869",
        "tag": "7",
        "resource_url": "harbor.sunvalley.com.cn/library/centos:7"
      }
    ],
    "repository": {
      "date_created": 1572414199,
      "name": "centos",
      "namespace": "library",
      "repo_full_name": "library/centos",
      "repo_type": "public"
    }
  },
  "operator": "robot$library-robot"
}
"""
    # payload = args.payload_json if args.payload_json else none
    # payload = args.payload_json if args.payload_json else none
    # request_body_dict = json.loads(payload)
    args = parser.parse_args([payload_json])
    # args = parser.parse_args()
    payload_str = args.payload if args.payload else "Error!! Couldn't get any payload!!"
    # print(payload_str)
    payload = json.loads(payload_str)
    for name in payload:
        print(name, '\t', payload[name])
        print(name, '\t', type(payload[name]))
    event_type = payload['type'] if 'type' in payload else "Error!! Couldn't get any type of event from the payload!!"
    if event_type == 'pushImage':
        event_type = 'push_image_handler'
    elif event_type == 'deleteImage':
        event_type = 'delete_image_handler'
    elif event_type == 'scanningCompleted':
        event_type = 'scanning_completed_handler'
    handler_module = importlib.import_module(".{}".format(event_type), 'webhook_handler')
    handler = handler_module.Handler(payload)
    # print(handler_module)
    # print(handler.event_type)
    print(handler.get_result())
