#!/usr/bin/env python3
"""Async comprehension module"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension."""
    return [i async for i in async_generator()]
