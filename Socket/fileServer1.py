"""
파일명 : fileServer1.py 
프로그램 설명 : 파일전송 서버 프로그램
"""

import socket
host = "127.0.0.1"
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()

# 클라이언트에서 보내온 파일 이름을 filename 변수에 저장한다.
filename1 = conn.recv(1024).decode('utf-8')

# 파일을 읽어서 클라이언트에게 전송한다.
f = open(filename1, "rb")
data = f.read()
conn.send(data)
f.close()

conn.close()  # 클라이언트 소켓 종료
s.close()     # 서버 소켓 종료