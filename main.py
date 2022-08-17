import asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    
    return {'data': 1}


async def count():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(count())
    
    value = await task1
    
    print(value)
    

asyncio.run(main())

# import asyncio

# async def count():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")

# async def main():
#     await asyncio.gather(count(), count(), count())

# if __name__ == "__main__":
#     import time
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")