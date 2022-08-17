import asyncio

async def send_email():
    print("hello")
    await asyncio.sleep(2)
    print("awake now")

async def t1():
    await t2()
    print("t1")
    
async def t2():
    await t3()
    print("t2")
    
async def t3():
    print("t3")
    
asyncio.run(t1())
    
