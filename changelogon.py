import rsa
import binascii
import base64
import urllib.request
import ssl
import json
import http.cookiejar
import os


ssl._create_default_https_context = ssl._create_unverified_context



def ChangeUI(ip,logfile):
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    #获取PubKey
    logfile.write(ip+'\n')
    postdata = '{"opr":"rsakey"}'.encode('utf-8')
    respstr = opener.open('https://%s/cgi-bin/login.cgi'%ip,postdata).read().decode('utf8')
    jresp = json.loads(respstr)
    if(jresp['success']!=True):
        print('Fetch PublicKey Failed!')
        return -1
    publickey = jresp['key']
    logfile.write(publickey+'\n')
    logfile.write(respstr+'\n')
    print(ip)

    #密码加密
    rsaPublickey = int(publickey,16)
    key = rsa.PublicKey(rsaPublickey,65537)
    crypto = rsa.encrypt("********".encode("utf8"),key)
    pwd = binascii.b2a_hex(crypto)
    logfile.write(str(pwd,'ascii')+'\n')
    logfile.write(respstr+'\n')
    print(respstr)

    #模拟登陆

    postdata = ('{"opr":"login", "data":{"user":"admin", "pwd":"%s"}}'%str(pwd,'ascii')).encode('utf8')
    req = urllib.request.Request('https://%s/cgi-bin/login.cgi'%ip,postdata)
    req.add_header('Referer','https://%s/login.html'%ip)
    req.add_header('Content-Type','Application/X-www-Form')
    resp = opener.open(req)
    respstr = resp.read().decode()
    jresp = json.loads(respstr)
    if(jresp['success']!=True):
        print('Login Failed!')
        print(jresp['msg'])
        return -1
    logfile.write(respstr+'\n')
    print(respstr)

    postdata = '{"opr" : "setAdvPage"}'.encode()
    resp = opener.open('https://%s/cgi-bin/adv_remind.cgi'%ip,postdata)
    respstr = resp.read().decode()
    jresp = json.loads(respstr)
    if(jresp['success']!=True):
        print("Change Ui Failed!")
        return -1
    logfile.write(respstr+'\n')
    print(respstr)

if(not os.path.exists('iplist.txt')):
    print('iplist.txt not found!')
    exit -1
iplist = open('iplist.txt','r')
flog = open('logfile.txt','w')
for ip in iplist:
    ip=ip.strip()
    try:
        ChangeUI(ip,flog)
    except Exception as e:
        print(e)