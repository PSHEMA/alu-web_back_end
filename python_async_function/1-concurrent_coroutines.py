#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
from typing import List
from asyncio import gather
from bisect import insort

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawns wait_random n times and returns list of delays in ascending order."""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        insort(delays, delay)
    
    return delays
