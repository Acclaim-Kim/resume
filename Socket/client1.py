import socket

host = '127.0.0.1'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print(s.recv(1024).decode())
s.send('반갑습니다.'.encode())

s.close()
