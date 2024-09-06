#!/usr/bin/env python3
""" Multiple coutines """

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_runtime(n: int, max_delay: int) -> float:
    """ measure runtime """
    start = time()
    await wait_n(n, max_delay)
    end = time()
    return end - start
