from encodings import utf_8
import requests
import base64
session=requests.session()
# proxy='127.0.0.1:8080'  #本地代理
# proxies={
#     'http':'http://'+proxy,
#     'https':'https://'+proxy
# }
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    #'Cookie':'security=medium; PHPSESSID=bdi0ak5mqbud69nrnejgf8q00u'
}
url="http://114.67.175.224:19756/"
getHeadersFlag=session.get(url).headers['flag']
postcontent=base64.b64decode(getHeadersFlag).decode('utf-8')
content=base64.b64decode(postcontent.split(': ')[1])
print(content)
data = {
    'margin':content
}
flag = session.post(url,data=data).content.decode('utf-8')
print(flag)