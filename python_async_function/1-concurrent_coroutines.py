#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait n """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return [await coro for coro in gather(*coroutines)]
