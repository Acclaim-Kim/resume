"""
파일명 : fileServer2.py
프로그램 설명 : 파일 전송 서버 프로그램
"""

import socket
import os

host = "127.0.0.1"       # 서비스 IP 주소 (127.0.0.1)
port = 8000              # 서비스 포트 번호
downloadFile = ""        # 클라이언트가 보내준 다운로드 할 파일명
fileFound = 0            # 파일의 존재여부 확인
sendMsg = ""             # 클라이언트에게 보내줄 메세지
data    = ""             # 파일의 내용을 읽어서 저장하는 변수
downloadDir  = "files"   # 파일 다운로드 디렉토리

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)

print(">>> 파일 전송 서버 프로그램 실행중 <<<")

conn, addr = s.accept()
print(addr[0] + " 에서 접속했습니다")

#클라이언트가 보내준 파일명을 받아서 downloadFile 변수에 넣는다.
downloadFile = conn.recv(1024).decode("utf-8")

print("다운로드 요청 파일 : " + downloadFile)

# 다운로드 디렉토리로 이동한다.
os.chdir(downloadDir)

# 다운로드 디렉토리의 파일 리스트를 확인해서 파일명이 존재하는지 체크한다.
# os.path.exists(path) 메소드를 사용하면 파일의 존재유무를 더 쉽게 확인할 수 있다.
#for i in os.listdir(".") :
#    # 클라이언트에서 요청한 파일명이 존재한다면 
#    # fileFound 변수에 1을 넣고 파일을 더이상 비교하지 않는다.
#    if i == downloadFile :
#        fileFound = 1
#        break

if os.path.exists(downloadFile):
    fileFound = 1

if fileFound == 1:
    # 파일이 존재하면 파일을 읽어서 클라이언트에게 전송한다.
    print(f"{downloadFile} 파일이 존재한다." )
    sendMsg = "200"
    conn.send(sendMsg.encode("utf-8"))
    f = open(downloadFile, "rb")

    while True:
        data = f.read(50)
        if not data:
            break
        conn.send(data)
        
    f.close()
else:
    print(f"{downloadFile} 파일이 존재하지 않습니다.")
    sendMsg = "404"
    conn.send(sendMsg.encode("utf-8"))

conn.close()
s.close()