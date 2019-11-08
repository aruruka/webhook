#!/usr/bin/env bash

webhook_home=/var/scripts

cd ${webhook_home}

if [[ $# -eq 1 ]]; then
    python ./harbor_webhook_test.py --json-string ${1}
else
    echo "You mustn't pass more than one arguments to me!"
fi