import requests

def download_picture(url,name):
    print(f'开始下载：{url}')
    response = requests.get(url)
    with open(f'abc{name}.gif','wb') as file:
        file.write(response.content)


def main():
    url_list = [
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif',
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif',
        'https://appdev.ahetc.com.cn/wmex-pmc/loading.gif'
    ]
    id = 1
    for url in url_list:
        download_picture(url,id)
        id += 1

main()