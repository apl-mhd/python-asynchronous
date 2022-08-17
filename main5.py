import asyncio

async def  data_reply():
    await asyncio.sleep(4)
    return {"data": 100}


async def task2():
    print('waiting for data')
    x = await data_reply()
    print(x)


asyncio.run(task2())