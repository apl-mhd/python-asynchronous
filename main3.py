import asyncio

async def task1():
    print('Send first email')
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print('First email reply')
    
async def task2():
    print('Send second email')
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print('Second email reply')
    

async def task3():
    print('Send third email')
    await asyncio.sleep(1)
    print('Third email reply')
    
asyncio.run(task1())
    