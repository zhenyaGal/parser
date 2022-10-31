from colorama import Fore, Style
import random
import string
import time
import os
import concurrent.futures
import urllib3
from inspect import getsourcefile
import full_scripts.downloading as download
import full_scripts.directory_check as checking_res

urllib3.disable_warnings()


def directory_create():
    """ Создаёт папку, в которую будут скачиваться изображения"""
    p = os.path.abspath(getsourcefile(lambda: 0))
    p = os.path.join(p[:-13] + 'pictures')
    if not os.path.exists(p):
        os.makedirs(p)


def input_actions():
    """ Ввод данных пользователем"""
    while True:
        try:
            choice = int(input())
        except:
            print('Enter the number in 1-3:')
        else:
            try:
                if choice == 1:
                    hours, minutes = input("Enter hours and minutes separated by a space: ").split()
                    end_time = int(hours)*3600 + int(minutes)*60
                    return choice, end_time
                elif choice == 2:
                    count = int(input("Enter the number of links: "))
                    return choice, count
                elif choice == 3:
                    size = int(input("Enter the size of downloading information in kb: "))
                    return choice, size
                else:
                    print('Enter the number in 1-3:')
            except:
                print('Enter the number in 1-3::')


def thread(th, choice, limit):
    """ Создаёт выбранное количество потоков и распределяет процессы по ним"""
    values = [0, 0, 0, 0]
    time_start = time.time()
    try:
        while values[choice] < limit:
            with concurrent.futures.ThreadPoolExecutor(th) as executor:
                end_random_list = []
                for i in range(0, th):
                    end_random_list.append(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7)))
                futures = []
                for end in end_random_list:
                    futures.append(executor.submit(download.check_img, end))
                for future in concurrent.futures.as_completed(futures):
                    if future.result():
                        values[3] = values[3] + int(future.result())
                        values[2] += 1
                    future.cancel()
                    values[1] = time.time()-time_start
        print(f'good:{Fore.GREEN}{values[2]}{Style.RESET_ALL}, time:{Fore.GREEN}{values[1]:.1f}{Style.RESET_ALL}, size:{Fore.GREEN}{values[3]}{Style.RESET_ALL}')
    except:
        print('Error in function thread')


def start_prog():
    """ Отвечает за запуск программы"""
    method_dict = {1: ["1) time ", "sec"],
                   2: ["2) link count ", "links"],
                   3: ["3) target size", "kb"]}
    try:
        th = int(input(Fore.GREEN + "Select Threads: " + Style.RESET_ALL))
    except:
        print('Error in function input')
    else:
        for value in method_dict.values():
            print(value[0])
        print((Fore.GREEN + "Choose method: " + Style.RESET_ALL))
        choice, limit = input_actions()
        thread(th, choice, limit)
        print(f"Target: imgur.com with {th} thread(s) for {limit} {method_dict[choice][1]}")
    print(checking_res.directory_open())


if __name__ == '__main__':
    directory_create()
    start_prog()
