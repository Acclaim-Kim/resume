"""
파일명 : fileClient1.py 
프로그램 설명 : 파일전송 클라이언트 프로그램
"""

import socket
import time

host = "127.0.0.1"
port = 8000

# 같은 PC에서 사용하기 때문에 서버의 파일명과 저장할 파일명을 다르게 설정했다.
filename1 = "파일전송1.txt"  # 서버의 파일명
filename2 = "파일전송2.txt"  # 다운로드 받아서 저장할 파일명

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((host,port))

s.send(filename1.encode('utf-8'))
data = ""

# 서버에서 보내온 파일 이름을 읽어서  변수에 저장한다.
f = open(filename2, "wb")

while True:
    data = s.recv(50)

    if not data:
        print(f"{filename1}: 파일 다운로드 완료")
        break

    f.write(data)

f.close()
s.close()