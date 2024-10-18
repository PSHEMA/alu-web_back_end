#!/usr/bin/env python3
""" 0x0B. Redis basics """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class to interact with Redis """
    def __init__(self):
        """ initialize redis connection and flush database """
        self._redis = redis.Redis()
        self._redis.flushdb()
        
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
