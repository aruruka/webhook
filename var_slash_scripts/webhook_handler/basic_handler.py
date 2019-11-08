#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bug-report: keraymondyan69gmail.com

import json


class BasicHandler:
    event_type: str
    occur_at: int
    event_data: dict
    operator: str

    def __init__(self, payload: dict):
        """Initialize basic handler for Harbor webhooks handler."""
        self.payload = payload
        self.event_type = payload['type']
        self.occur_at = payload['occur_at']
        self.event_data = payload['event_data']
        self.operator = payload['operator']

    def get_result(self, *args):
        """Run handle method and packs result into JSON."""
        result = self.handle(*args)
        return json.dumps(result)

    def handle(self, *payload):
        """Method that should be overridden inside inherited classes."""
        pass
