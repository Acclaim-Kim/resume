"""
파일명 : client3.py
프로그램 설명 : 클라이언트 프로그램
"""
import socket

host = "127.0.0.1" # 접속할 서버의 IP주소를 지정한다.
port = 8000 # 접속할 서버의 포트번호를 지정한다.

# 1. 통신연결 단계
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((host,port))

# 2. Data 송수신 단계
print("서버로 접속한다.")

while True:
    print(s.recv(1024).decode('utf-8'))
    data = input("서버로 전송할 메세지를 입력하세요 : ")
    s.send(data.encode('utf-8'))

# 3. 통신해제 단계
s.close()