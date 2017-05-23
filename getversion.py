import ssl
import urllib.request

KEYWORD = "17-05-19"

ssl._create_default_https_context = ssl._create_unverified_context
ipfile = open('iplist.txt','r')
fout = open('result.txt','w')
for line in ipfile:
    line = line.rstrip('\n')
    url = "https://%s/cgi-bin/login.cgi"%(line)
    postdata = '{"opr":"version"}'.encode('utf-8')
    version = ''
    try:
        version = urllib.request.urlopen(url,postdata).read().decode('utf-8')
    except urllib.error.URLError as error:
        if(error.reason.errno==10060):
            print(line+'\t'+'不在线')
            fout.write(line+'\t'+'不在线\n')
            continue
        else:
            print(error)
    if( version == ''):
        print('ERROR:Empty')
        continue
    if( version.find(KEYWORD) == -1 ):
        print(line+'\t'+'未打补丁')
        fout.write(line+'\t'+'未打补丁\n')
    else:
        print(line+'\t'+'正常')
        fout.write(line+'\t'+'正常\n')
fout.close()