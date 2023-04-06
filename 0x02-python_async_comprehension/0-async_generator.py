#!/sur/bin/env python3
"""
This module contains a coroutine, async_generator, with no arguments looping
 10 times, each time asynchronously wait 1 second, then yield a random number
 between 0 and 10. random module is used.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    for i in range(0, 10):
        await asyncio.sleep(1)
        ran = random.uniform(0, 10)
        yield ran
