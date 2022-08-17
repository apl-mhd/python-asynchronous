import asyncio
from unittest import async_case


async def main():
    task = asyncio.create_task(other_function())
    await task
    print("A")
    await asyncio.sleep(1)
    print("b")
    
async def other_function():
    print("1")
    await asyncio.sleep(1)
    print("2")
    


asyncio.run(main())
