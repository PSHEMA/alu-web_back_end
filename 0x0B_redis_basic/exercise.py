#!/usr/bin/env python3
""" 0x0B. Redis basics """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count and invokes the original method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[bytes, str, int, float]:
        """ get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """ get string from redis """
        return self.get(key, lambda x: x.decode('utf-8'))
    
    def get_int(self, key: str) -> int:
        """ get int from redis """
        return self.get(key, int)
    
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in redis """
        return super().store(data)
