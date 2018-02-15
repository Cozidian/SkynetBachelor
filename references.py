#!/usr/bin/env python
# -*- coding: utf-8 -*-


def remove_empty_lines(f):
    """TODO: Docstring for remove_empty_lines.
    :returns: filled lines

    """
    for l in f:
        line = l.rstrip()
        if line:
            yield line


def open_file():
    """TODO: Docstring for open_file.
    :returns: List of url

    """
    url_list = []
    try:
        with open('./url.txt', 'r') as f:
            for line in remove_empty_lines(f):
                url_list.append(line)
    except Exception as e:
        raise e
    return url_list


def read_reference_list(reference_list):
    """TODO: Docstring for read_reference_list.
    :returns: url

    """
    pass


print(open_file())
