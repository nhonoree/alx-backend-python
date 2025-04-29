#!/usr/bin/env python3
"""Measure runtime of async comprehensions"""
import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Runs async_comprehension 4 times in parallel and measures the time."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
