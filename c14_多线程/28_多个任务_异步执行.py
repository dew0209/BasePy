import asyncio


async def work(n,delay):
    print(f'work{n}开始')
    print(f'work{n}执行中.......')
    await asyncio.sleep(delay)
    print(f'work{n}结束')
    return f'work{n}的返回值'

async def main():
    print('main开始')

    # 写法一：
    # asyncio.create_task 会把一个协程的对象包装成一个可被事件循环调度的任务，并注册到事件循环中
    # task1 = asyncio.create_task(work(1,2))
    # task2 = asyncio.create_task(work(2,2))
    # task3 = asyncio.create_task(work(3,2))
    #
    # res1 = await task1
    # print(res1)
    #
    # res2 = await task2
    # print(res2)
    #
    # res3 = await task3
    # print(res3)

    # 写法二：
    result = await asyncio.gather(work(1,2),work(2,2),work(3,2))
    

    print('main结束')
    return '我是main的返回值'

res = asyncio.run(main())
print(res)