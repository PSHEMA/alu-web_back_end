#!/usr/bin/env python3
""" Filtered logger """

import re
from typing import List


def filter_datums(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Redact message """
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]*', f'{field}={redaction}', message)
    return message
