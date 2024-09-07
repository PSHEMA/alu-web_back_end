#!/usr/bin/env python3
""" Measures runtime """

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


def measure_runtime() -> float:
    """ Measures runtime """
    start = time.perf_counter()
    asyncio.run(async_comprehension())
    end = time.perf_counter()
    return (end - start)
