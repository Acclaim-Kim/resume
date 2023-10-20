"""
파일명 : chatServer.py
프로그램 설명 : 채팅 서버 프로그램
"""

import socket

host = ""           # Listen할 IP주소
port = 8000         # Listsen할 포트번호
recv_msg = ""  # 클라이언트에서 온 Data를 저장할 변수
send_msg = ""  # 클라이언트로 보낼 Data를 저장할 변수

# 1. 통신연결 단계
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)
conn, addr = s.accept()
print("[클라이언트님이 대화방에 들어왔습니다]")

# 2. Data 송수신 단계
while True:
    # Data 송신
    send_msg = input("Server : ")

    # Client로 보낼 Data를 입력 받아 utf-8로 인코딩한 후 Client로 전송한다.
    conn.send(send_msg.encode('utf-8'))

    # 입력된 자료가 "quit" 이면 프로그램을 종료한다.
    if send_msg == "quit":
        break

    # Data 수신
    recv_msg = conn.recv(1024).decode('utf-8')
    print("Client : %s" %(recv_msg))

    # 입력된 자료가 "quit" 이면 프로그램을 종료한다.
    if recv_msg == "quit":
        break

# 3. 통신해제 단계
print("대화가 종료 되었습니다.")
conn.close()  # 클라이언트 소켓 종료
s.close()     # 서버 소켓 종료