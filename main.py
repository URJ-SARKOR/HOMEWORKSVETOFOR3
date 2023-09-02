import time
import asyncio
from threading import Thread


# АСИНХРОННОСТЬ
async def red():
    await asyncio.sleep(5)
    print('Красный')


async def yellow():
    await asyncio.sleep(7)
    print('Желтый')


async def green():
    await asyncio.sleep(9)
    print('Зеленый')


async def main():
    task1 = asyncio.create_task(red())
    task2 = asyncio.create_task(yellow())
    task3 = asyncio.create_task(green())

    await task1
    await task2
    await task3


asyncio.run(main())
print('Старт!!!')
