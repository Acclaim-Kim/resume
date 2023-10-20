"""
파일명 : chatClient.py
프로그램 설명 : 채팅 클라이언트 프로그램
"""

import socket
host = "127.0.0.1"
port = 8000

# utf-8 인지 확인
#import sys
#print(sys.getdefaultencoding())

recv_msg = ""  # 서버에서 온 Data를 저장할 변수
send_msg = ""  # 서버로 보낼 Data를 저장할 변수

# 1. 통신연결 단계
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((host,port))

# 2. Data 송수신 단계
while True:
    # Data 수신 부분
    # Server 에서 온 Data를 utf-8로 인코딩한 후 화면에 출력한다.
    # print(s.recv(1024).decode('utf-8'))
    recv_msg = s.recv(1024).decode('utf-8')
    print("Server : " + recv_msg)

    # 입력된 Data가 "quit" 이면 프로그램을 종료한다.
    if recv_msg == "quit":
        break

    # Data 송신 부분
    # Server로 보낼 Data를 입력 받아 utf-8로 인코딩한 후 서버로 전송한다.
    send_msg = input("Client : ")
    s.send(send_msg.encode('utf-8'))

    # 입력된 Data가 "quit" 이면 프로그램을 종료한다.
    if send_msg == "quit":
        break

# 3. 통신해제 단계
print("대화가 종료되었습니다")
s.close()
