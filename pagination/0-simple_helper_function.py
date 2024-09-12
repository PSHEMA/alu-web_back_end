#!/usr/bin/env python3
""" Simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ index range """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
