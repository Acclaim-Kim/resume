"""
파일명 : exFile2.py 
프로그램 설명 : 파일 입출력 예제 (파일에서 데이터 읽기)
"""

# 저장된 파일: exFile1.txt
filename = 'exFile1.txt'
# 1. 파일 열기 (읽기 모드)
# 파일이 존재하지 않으면 에러가 발생된다. (주의!)
# 파일이 존재하면 에러가 발생하지 않는다.
# r, rt: 읽기 권한
# filename 변수에 저장된 파일을 읽기 모드로 f라는 변수에 오픈한다.
f = open(filename, 'rt', encoding = 'utf-8')

# 2. 파일 처리 (읽기)
# 형식: 
# 변수명.read():  파일 전체 읽기
# 변수명.read(size): 파일의 size 만큼 읽기
# 리턴값: 읽은 문자열을 반환한다.
#
# read() 메소드(함수)는 리턴값이 있으므로 두 가지 방식을 사용한다.
# 리턴값을 바로 출력하는 경우: print(f.read())
# 리턴값을 변수에 저장해서 활용하는 경우
# data = f.read()   # "Hello"
# print(data)
print(f.read())

# 3. 파일 닫기 
# 형식: 
# 변수명.close()
f.close()