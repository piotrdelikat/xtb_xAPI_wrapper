import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'ws.xapi.pro/demo'
port = 5124

request = {"command": "getServerTime"}


s.connect((server, 5124))
s.send(json.dumps(request))
result = s.recv(4096)

while len(result) > 0:
    print(result)
    result = s.recv(1024)
