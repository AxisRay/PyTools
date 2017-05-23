from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from telegram import bot
import datetime

# Listen Address
ADDR = ''
# Listen Port
PORT = 8888

CODE = 'UTF-8'
FILE = './log.txt'

CHAT_ID = '329222612'
TOKEN = '334041002:AAG9fU8gjrovlW6VJqw02by7jQo2jrEHf9c'


class WebRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        text = data.decode(CODE)
        print('Content:' + text)
        self.record(text)
        self.send_response(200)
        self.send_header('Content-Length', '0')
        self.end_headers()
        self.msgbot(msgprocess(text))

    def record(self, text):
        f = open(FILE, 'a')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(now + "\n")
        f.write('Content:\n' + text + "\n")
        f.close()

    def msgbot(self, text):
        mybot = bot.Bot(TOKEN)
        mybot.sendMessage(CHAT_ID, text)

    def msgprocess(self, text):
        msg=""
        textlines = text.splitlines()
        msg+="Time:"+textlines[0]
        for i,line in enumerate(textlines):
            if "eth0" in line:
                msg+="eth0"+textlines[i+1]
            if "ppp" in line:
                msg+="ppp"+textlines[i+1]
        return msg

server = HTTPServer((ADDR, PORT), WebRequestHandler)
print("Server start!")
server.serve_forever()
