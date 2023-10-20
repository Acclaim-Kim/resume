"""
파일명 : fileClient2.py
프로그램 설명 : 파일 전송 클라이언트 프로그램
"""

import socket

host = "127.0.0.1"      # 접속할 서버의 IP주소
port = 8000             # 접속할 서버의 서비스 포트 번호
downloadFile = ""       # 서버가 보내준 다운로드 할 파일명
downloadDir  = "data"   # 다운로드 디렉토리
recvMsg = ""            # 서버에게 받은 메세지
data    = "temp"        # 파일의 내용을 읽어서 저장
count = 1               # 다운로드 카운트 수
downloadBuffSize = 8192 # 파일 다운로드 사이즈

# 서버에 접속한다.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((host,port))

# 다운로드할 파일명을 입력한다.
downloadFile = input("다운로드 받을 파일명 : ")

# 다운로드할 파일명을 서버에 전송한다.
s.send(downloadFile.encode("utf-8"))

# 서버에서 보내준 상태코드를 받는다.
# 상태코드 : 
# 200 : 파일이 존재함
# 404 : 파일이 존재하지 않음
recvMsg = s.recv(3).decode("utf-8")

# 서버에서 보내준 상태코드를 분석한다.
# 파일이 존재하는 경우
if(recvMsg == "200"):
    print("%s 파일을 다운로드 한다." %(downloadFile))

    data = s.recv(downloadBuffSize)
    f = open("data\\" + downloadFile, "wb")

    while data:
        print("Download count : %d\r" %(count), end='',flush=True)
        count += 1
        f.write(data)
        data = s.recv(downloadBuffSize)
    f.close()
    print("\n다운로드가 완료되었습니다.")

# 파일이 존재하지 않는 경우
elif (recvMsg == "404"):
    print("%s 파일이 존재하지 않습니다." %(downloadFile))

s.close()