#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

EMAIL = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'


def prepare_email(appointments):
    "Returns body of the email"
    i = 0
    new = []
    for appointments[i] in appointments:
        new.append(EMAIL.format(appointments[i][0], appointments[i][1]))
        i += 1
    return new
