"""
파일명 : jumsuClassSQLite.py
프로그램 설명 : class + sqlite3를 이용한 점수 관리 프로그램
"""

import os, sqlite3
import time
import getpass
import sys

# 클래스 정의
class Jumsu:
    """Jumsu 클래스"""

    def __init__(self):
        """생성자"""
        try: 
            dbName = 'sqlite/jumsu.db'
            self.conn = sqlite3.connect(dbName) # 커넥션 객체 생성
            self.cur = self.conn.cursor() # 커서 객체 생성
        except: 
            print('DB 파일을 확인해주세요!')
            sys.exit()


    def __del__(self):
        """소멸자"""
        self.cur.close() #커서 객체 종료
        self.conn.close() #커넥션 객체 종료

    def addJumsu(self):
        """점수 추가"""
        print('>>>점수 추가 <<<')
        
        # 1. wajtn dlqfur
        name = input("이름: ")
        kor = input("국어 점수: ")
        eng = input("영어 점수 :")
        math = input("수학 점수 :")

         # 각 점수의 값이 없으면 0을 넣고 있으면 int()함수로 변환해서 넣는다.
        # 3항 연산자를 사용한 경우
        # 조건식이 참이면 값1을 변수에 넣고 거짓이면 값2를 변수에 넣어라.
        # 형식 : 변수 = 값1 if 조건식 else 값2

        kor  = 0 if kor  == '' else int(kor)
        eng  = 0 if eng  == '' else int(eng)
        math = 0 if math == '' else int(math)

        # 2. 점수 계산
        total = kor + eng + math  #총점
        average = total / 3  # 평균

        # 점수를 출력하는 부분
        print(">>> 점수의 결과 <<<\n"
              f"국어점수 : {kor}\n"
              f"영어점수 : {eng}\n"
              f"수학점수 : {math}\n"
              f"총점 : {total}\n"
              f"평균 : {average:.2f}\n")  
        yesno = input('입력한 내용을 저장하겠습니까? (y/n default y) :')
        #if yesno == '' or yesno = 'y' or yesno = 'Y':
        if yesno in ('', 'y', 'Y'):
            # 점수를 DB에 저장하는 부분
            query  = f"""INSERT INTO jumsu VALUES(
                      NULL,'{name}',{kor}, {eng}, {math}, {total}, {average:.2f})""" 

            try:
                self.cur.execute(query) 
            except:
                print('DB 에러가 발생했습니다.')
                print('프로그램을 종료했습니다.')
                sys.exit()

            self.conn.commit()
            print(f'{name} 사용자의 점수를 추가했습니다.')
        else:
            print(f'{name} 사용자의 점수 입력을 취소했습니다.')

    def viewJumsu(self):
        """점수 확인"""
        print('>>>점수 확인<<<')

        try:
            # DB에 저장된 점수를 출력하는 부분
            # no 컬럼을 이용해서 내림차순 정렬(DESC) 정렬한다
            query = "SELECT* FROM junsu ORDER BY no DESC"
            self.cur.execute(query) # 쿼리 실행
        except:
            print('DB를 확인해주세요.')
            sys.exit()
        
        # 자료의 수만큼 반복해서 출력한다.
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
        for no, name, kor, eng, math, total, average in self.cur:
            print(f'{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{average}')
            
    def serachJumsu(self):
        """점수 검색"""
        
        print('>>> 점수 검색 <<<')
        foundUser = 0
        searchName = input('이름 (Enter : 검색 취소): ')

        if not searchName: # searchName = ''
            print('검색을 취소했습니다')
            return #함수의 종료는 return 또는 모든 코드가 끝나면
        
        try:
            # DB에 저장된 점수를 출력하는 부분
            query = f"SELECT* FROM jumsu Where name = '{searchName}'"
            self.cur.execute(query) #쿼리 실행
        except:
            print('DB에 에러가 발생했습니다.')
            print('프로그램을 종료합니다.')
            sys.exit()


        print('번호\t이름\t국어\t영어\t수학\t총점\t평균')
        for no, name, kor, eng, math, total, average in self.cur:
            print(f'{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{average}')
            foundUser = 1
        
        if foundUser == 0:
            print(f'{searchName} 사용자가 없습니다.')

    def delJumsu(self):
        """점수 삭제"""
        delName = input('이름 (Enter : 삭제 취소): ')

        if not delName: # delName = ''
            print('삭제를 취소했습니다')
            return #함수의 종료는 return 또는 모든 코드가 끝나면
        
        try:
            # DB에 저장된 점수를 삭제하는 코드
            query = f"DELETE* FROM jumsu Where name = '{delName}'"
            self.cur.execute(query) #쿼리 실행
            self.conn.commit() # 여기선 꼭 실행해야함
        except:
            print('DB에 에러가 발생했습니다.')
            print('프로그램을 종료합니다.')
            sys.exit()


    def helpJumsu(self):
        """점수 도움말"""
        
        help_msg  = ">>> 도움말 <<<\n"
        help_msg += "- 점수 추가 : 점수를 추가합니다.\n"
        help_msg += "- 점수 출력 : 점수를 출력합니다.\n"
        help_msg += "- 점수 검색 : 점수를 검색합니다.\n"
        help_msg += "- 점수 삭제 : 점수를 삭제합니다.\n"
        print(help_msg)

    def aboutJumsu(self):
        """점수 프로그램 정보"""
    
        about_msg  = ">>> 점수 프로그램 (v1.0) <<<\n"
        about_msg += "- 점수 추가 기능\n"
        about_msg += "- 점수 출력 기능\n"
        about_msg += "- 점수 검색 기능\n"
        about_msg += "- 점수 삭제 기능\n"
        about_msg += " \n"
        print(about_msg)

    def menuJumsu(self):
        """점수 menu"""
        
        MENU  = "1. 점수 추가\n"
        MENU += "2. 점수 확인\n"
        MENU += "3. 점수 검색\n"
        MENU += "4. 점수 삭제\n"
        MENU += "5. 점수 도움말\n"
        MENU += "6. 점수 프로그램 정보\n"
        MENU += "q. 프로그램 종료\n"
        print(MENU)

    def loginJumsu(self):
        """점수 로그인"""
        print('>>>  주소록 로그인 <<<')
        count = 3 # 로그인 횟수
        i = 1
        dbUserid = 'python'
        dbUserpass = '1234'

        while i <= count:
            
            inputUserid = input('사용자: ')
            inputUserpw = getpass.getpass('비밀번호: ') #비밀번호를 보여주지 않음
            if dbUserid == inputUserid and dbUserpass == inputUserpw:
                return True
            count -+ 1
        else:
            return False




    def jumsuMain(self):
        """점수 main 메소드"""
        
        if  True # self.loginJumsu():
            print('로그인에 성공했습니다')
            time.sleep(2)
        else:
            print('로그인에 실패했습니다!!!')
            print('프로그램을 종료합니다')
            sys.exit()


        while True: # While 1:
            os.system('cls')
            print('>>> SQLite3용 점수 입력 프로그램 <<<\n')
            self.menuJumsu() #메뉴 출력

            x = input('선택 >>> ') #메뉴 입력
            
            #메뉴 체크
            if not x:
                continue
            elif x == '1': # 점수 추가
                self.addJumsu()
            elif x == '2': # 점수 확인
                self.viewJumsu()
            elif x == '3': # 점수 검색
                self.searchJumsu()
            elif x == '4': # 점수 삭제
                self.delJumsu
            elif x == '5': # 도움말 출력
                self.helpJumsu()
            elif x == '6': # 프로그램 정보
                self.aboutJumsu()
            elif x in ('q', 'Q'): #x == 'q'or x == 'Q': # 점수 프로그램 종료
                break
            else:
                print('1 ~ 6 or q 중에서 입력해야 합니다.')

            input('Enter를 누르세요...')

# 객체(instance 생성)
# jumsu = Jumsu()
# jumsu.jumsuMain()

# 클래스 정의
class Jumsu2(Jumsu):
    """Jumsu2 클래스"""
    pass

    def editJumsu(self):
        """점수 수정"""

        print(">>> 점수 수정 <<<")
        editName = input("이름: ")
        try:
            # DB에 저장된 점수를 출력하는 부분
            query = f"SELECT* FROM jumsu Where name = '{editName}'"
            self.cur.execute(query) #쿼리 실행
        except:
            print('DB에 에러가 발생했습니다.')
            print('프로그램을 종료합니다.')
            sys.exit()

        # 쿼리 결과 가져오기기
        # .fetchall(): 전체 ROW를 리스트로 각 ROW를 튜플로 반환하는 메서드
        # .fetchone(): 하나의 ROW를 튜플로 반환하는 메서드
        
        row = self.cur.fetchall()
        if not row: # 사용자가 존재하지 않으면
            print(f'{editName} 사용자가 없어서 수정할 수 없습니다')
            return

        
        print(row)
        editNo = row[0][0]


        kor = input("국어 점수: ")
        eng = input("영어 점수 :")
        math = input("수학 점수 :")

         # 각 점수의 값이 없으면 0을 넣고 있으면 int()함수로 변환해서 넣는다.
        # 3항 연산자를 사용한 경우
        # 조건식이 참이면 값1을 변수에 넣고 거짓이면 값2를 변수에 넣어라.
        # 형식 : 변수 = 값1 if 조건식 else 값2

        kor  = 0 if kor  == '' else int(kor)
        eng  = 0 if eng  == '' else int(eng)
        math = 0 if math == '' else int(math)

        # 2. 점수 계산
        total = kor + eng + math  #총점
        average = total / 3  # 평균

        # 점수를 출력하는 부분
        print(">>> 점수의 결과 <<<\n"
              f"국어점수 : {kor}\n"
              f"영어점수 : {eng}\n"
              f"수학점수 : {math}\n"
              f"총점 : {total}\n"
              f"평균 : {average:.2f}\n")  
        yesno = input('입력한 내용을 저장하겠습니까? (y/n default y) :')
        #if yesno == '' or yesno = 'y' or yesno = 'Y':
        if yesno in ('', 'y', 'Y'):
            # 점수를 DB에 저장하는 부분
            query  = f"""UPDATE jumsu SET
                        name ='{editName}',
                        kor = '{kor},
                        eng = {eng},
                        math = {math},
                        total = {total},
                        average = {average:.2f}
                        WHERE  no = '{editNo}'"""

            try:
                self.cur.execute(query) 
            except:
                print('DB 에러가 발생했습니다.')
                print('프로그램을 종료했습니다.')
                sys.exit()

            self.conn.commit()
            print(f'{editName} 사용자의 점수를 수정했습니다.')
        

    def menuJumsu(self):
        """점수 menu"""
        
        MENU  = "1. 점수 추가\n"
        MENU += "2. 점수 확인\n"
        MENU += "3. 점수 검색\n"
        MENU += "4. 점수 삭제\n"
        MENU += "5. 점수 수정\n"
        MENU += "6. 점수 도움말\n"
        MENU += "7. 점수 프로그램 정보\n"
        MENU += "q. 프로그램 종료\n"
        print(MENU)

    def jumsuMain(self):
            """점수 main 메소드"""
            
            if  True # self.loginJumsu():
                print('로그인에 성공했습니다')
                time.sleep(2)
            else:
                print('로그인에 실패했습니다!!!')
                print('프로그램을 종료합니다')
                sys.exit()


            while True: # While 1:
                os.system('cls')
                print('>>> SQLite3용 점수 입력 프로그램 <<<\n')
                self.menuJumsu() #메뉴 출력

                x = input('선택 >>> ') #메뉴 입력
                
                #메뉴 체크
                if not x:
                    continue
                elif x == '1': # 점수 추가
                    self.addJumsu()
                elif x == '2': # 점수 확인
                    self.viewJumsu()
                elif x == '3': # 점수 검색
                    self.searchJumsu()
                elif x == '4': # 점수 삭제
                    self.delJumsu
                elif x == '5': # 점수 수정
                    self.editJumsu
                elif x == '6': # 도움말 출력
                    self.helpJumsu()
                elif x == '7': # 프로그램 정보
                    self.aboutJumsu()
                elif x in ('q', 'Q'): #x == 'q'or x == 'Q': # 점수 프로그램 종료
                    break
                else:
                    print('1 ~ 7 or q 중에서 입력해야 합니다.')

                input('Enter를 누르세요...')

jumsu2 = Jumsu2()
jumsu2.jumsuMain()