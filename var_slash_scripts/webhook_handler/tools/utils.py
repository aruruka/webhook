#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bug-report: keraymondyan69gmail.com

import subprocess


class OSCommand:
    """
    command: command line list, e.g. ['ls', '-h']
    """
    command_line: list

    def __init__(self, command):
        self.command_line = command
        # self.output = ''
        # self.error_output = ''
        # self.return_code = ''

    def run(self):
        # print(self.command_line)
        return subprocess.run(self.command_line, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.output, self.error_output, self.return_code = p.stdout, p.stderr, p.returncode


def unique(repetitive_list):
    """
    To check if two
    to get unique values from list
    using set
    :param repetitive_list: A list with repetitive items.
    :return: A new list with uniq items.
    """
    list_set = set(repetitive_list)
    unique_list = list(list_set)
    return unique_list
