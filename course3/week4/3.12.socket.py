import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#encode converts the unicode(usually UTF-8) into bytes
mysock.send(cmd)

while True:
    data = mysock.recv(512) #we recieve here is bytes
    if len(data) < 1:
        break
    print(data.decode(),end='')
    #decode converts the bytes into unicode

mysock.close()
