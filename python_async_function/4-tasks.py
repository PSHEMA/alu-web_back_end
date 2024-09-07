#!/usr/bin/env python3
""" task 4 """

import asyncio
from typing import List
from asyncio import gather

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return a list of all the delays (float values). """
    tasks = [task_wait_random(max_delay) for x in range(n)]
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
