#!/usr/bin/env python3
""" Multiple coroutines """

import asyncio
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait n """
    tasks = [wait_random(max_delay) for x in range(n)]
    data_list = await gather(*tasks)
    new_list = []

    while data_list:
        minimum = data_list[0]
        for x in data_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        data_list.remove(minimum)

    return new_list
