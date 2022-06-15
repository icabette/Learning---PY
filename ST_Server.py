from pickle import TRUE
from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 7979))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'에서 접속이 확인되었습니다.')

while TRUE:
    data = connectionSock.recv(1024)
    strData = data.decode('utf-8')
    print('받은 데이터 : ', strData)
    if strData == "exit":
        connectionSock.send('Connection is closed'.encode('utf-8'))
        connectionSock.close()
        break

"""
connectionSock.send('I am a server.'.encode('utf-8'))
print('메시지를 보냈습니다.')
"""
