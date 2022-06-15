from pickle import TRUE
from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.100.62', 7979))

print('연결 확인 됐습니다.')

while TRUE:
    strData = input()
    clientSock.send(strData.encode('utf-8'))
    if strData == "exit":
        data = clientSock.recv(1024)
        print('받은 데이터 : ', data.decode('utf-8'))
        clientSock.close()
        break
