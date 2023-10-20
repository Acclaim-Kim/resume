"""
파일명 : server2.py
프로그램 설명 : 서버 프로그램
"""

import socket
host = ""   # 현재 서버에 사용중인 모든 IP주소를 지정한다.
port = 8000 # 다른 프로세스가 사용하지 않는 포트로 지정한다.

# 1. 통신연결 단계
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 주소를 재사용하는 소켓 옵션
s.bind((host,port)) 
s.listen(5)
conn, addr = s.accept()

# 2. Data 송수신 단계
print("클라이언트가 접속했습니다")
data = input("클라이언트로 전송할 메세지를 입력하세요 : ")
conn.send(data.encode('utf-8'))
print(conn.recv(1024).decode('utf-8'))

# 3. 통신해제 단계
conn.close()
s.close()