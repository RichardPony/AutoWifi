#用于自动登录BISTU的校园网
import requests
Login_head = '''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:max-age=0
Connection:keep-alive
Content-Length:149
Content-Type:application/x-www-form-urlencoded
Cookie:program=beijing-information; vlan=0; ip=10.3.131.236; md5_login2=2017011398%7C00107591
Host:192.168.7.71
Origin:http://192.168.7.71
Referer:http://192.168.7.71/a70.htm
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'''
def getHeaders(raw_head):
    headers = {}
    for raw in raw_head.split('\n'):
        headerkey, headerValue = raw.split(':', 1)
        headers[headerkey] = headerValue
    return headers
header = getHeaders(Login_head)
s = requests.session()
url = "http://192.168.7.71/a70.htm"
FormData = {
    '0MKKey': '123456',
    'DDDDD':'2017011398',#此处填写学号
    'Login':'',
    'R1': '0',
    'R2':'',
    'R3': '0',
    'R6': '0',
    'buttonClicked':'',
    'cmd':'',
    'err_flag':'',
    'para': '00',
    'password':'',
    'redirect_url':'',
    'upass': '0010****',#登录校园网用的密码
    'user':'',
    'username':''
}
res = s.post(url,FormData,headers=header)
print(res)