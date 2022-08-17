import asyncio
from cProfile import run

async def fetch_data():
    print("Fetching data")
    await asyncio.sleep(6)
    print("data returned")
    return {'data': 100}
    
async def task2():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)
        
async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(task2())
    
    data  = await x
    print(data)
    await y 
    
    
asyncio.run(main())