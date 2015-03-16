#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


def get_party_stats(families, table_size=6):

    """Returns total number of attendiees and total number of tables"""
    i = 0
    add = 0
    tables = len(families)
    for families[i] in families:
        add += len(families[i])
        if len(families[i]) > table_size:
            tables += 1
        i += 1
    return add, tables
