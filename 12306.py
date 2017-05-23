#!/usr/bin/python3
import urllib.request
import time
import ssl
import json
import email.mime.multipart
import email.mime.text
import smtplib

def SendMail(information,leftTickets):
    msg=email.mime.multipart.MIMEMultipart()
    msg['from']='446015875@qq.com'
    msg['to']='rayleesky@outlook.com'
    msg['subject']='余票信息！！！！硬卧剩余：%s'%leftTickets
    content='''
请注意：

车票信息：
%s

    '''%information
    txt=email.mime.text.MIMEText(content,'plain','UTF8')
    msg.attach(txt)
    smtp=smtplib.SMTP()
    smtp.connect('smtp.qq.com','587')
    smtp.starttls()
    smtp.login(msg['from'],'eilsymqogihqcabb')
    smtp.sendmail(msg['from'],msg['to'],str(msg))
    smtp.quit()

def CheckTicket(from_station,to_station,train_no,train_date):
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'\
    .format(train_date,from_station,to_station)
    ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.request.urlopen(url).read()
    html = data.decode('utf8')
    return json.loads(html)

to_station='SZQ'
from_station='TAK'
train_no='T398'
train_date='2016-10-06'
interval=30
left=3
message='列车运行图调整,暂停发售'


while(1):
    current_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    info=CheckTicket(from_station,to_station,train_no,train_date)
    controlled_train_message=info['data']['datas'][0]['controlled_train_message']
    yw_num=info['data']['datas'][1]['yw_num']
    if(yw_num!='无'):
        infodata=json.dumps(info['data']['datas'][1],ensure_ascii=False,indent=4)
        SendMail(infodata,yw_num)
        interval=180
        left-=1
        print('Time:%s\tMsg:Mail have been sent,left %d'%(current_time,left))
        if(left<0):
            exit(0)
    else:
        print('Time:%s\tMsg:%s'%(current_time,yw_num))
        interval=30
        left=3
    time.sleep(interval)
