import random

import aiohttp
import asyncio

async def download_picture(session, url, id):
    print(f'开始下载：{session}')
    # 发送网络请求，获取这张图片，请求发出去后，要等待服务器把数据返回，等的这段时间就是I/O等待
    response = await session.get(url)
    # 等待数据(图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是I/O等待)
    content = await response.read()
    # 保存图片到本地
    with open(f'abcd{id}.gif', 'wb') as f:
        f.write(content)
    # 释放连接资源（告诉 aiohttp，这个连接我不用了，你可以回收了）
    await response.release()
    print('下载完毕')


async def main():
    url_list = [
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif',
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif',
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif'
    ]
    # 创建会话对象（发送请求的工具）
    session = aiohttp.ClientSession()
    # 创建多个协程对象
    coroutine_list = [download_picture(session,url, random.randint(1,100)) for url in url_list]
    await asyncio.gather(*coroutine_list)
    # 关闭会话
    await session.close()


asyncio.run(main())