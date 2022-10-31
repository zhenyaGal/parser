import requests
from fake_useragent import UserAgent
from colorama import Fore, Style
import os


def ip_check(url):
    """ Проверяет доступность сайта"""
    ua = UserAgent()
    proxies = {'http': 'socks5://127.0.0.1:9050',
               'https': 'socks5://127.0.0.1:9050'
               }
    headers = {'User-Agent': ua.random}
    try:
        res = requests.get(url, headers=headers, proxies=proxies, timeout=20,
                           verify=False, stream=True)
    except (Exception, KeyboardInterrupt):
        print('Error in function requests.get')
        return False
    else:
        if res.status_code != 200:
            os.system('service tor restart')
            ip_check(url)
        else:
            return res


def downloading(res, name):
    """ Скачивает найденное изображение в папку"""
    res.raise_for_status()
    with open('pictures/' + name + '.jpg', 'wb') as f:
        for i in res.iter_content(chunk_size=64000):
            f.write(i)


def check_img(end):
    """ Проверяет существование картинке по данному адресу"""
    url = f'https://i.imgur.com/{end}.jpeg'
    if (res := ip_check(url)) and 'PNG' not in res.text:
        print(url, Fore.GREEN + 'GOOD', Style.RESET_ALL)
        downloading(res, end)
        file_size = os.stat('pictures/' + end + '.jpg').st_size/(2**10)
        return file_size
    else:
        print(url, Fore.RED + 'BAD', Style.RESET_ALL)
        return False
