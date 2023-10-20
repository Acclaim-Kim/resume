import socket

host = '127.0.0.1'
port = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind((host, port))
s.listen(5)

conn, addr = s.accept()

conn.send('안녕하세요.'.encode())
print(conn.recv(1024).decode())

conn.close()
s.close()
