"""
파일명 : exFile1.py 
프로그램 설명 : 파일 입출력 예제 (파일에 데이터 쓰기)
"""
filename = "exFile1.txt"
# 1. 파일 열기 (쓰기모드)
# 파일이 존재하면 기존에 저장된 파일의 내용은 전부 날라간다. (주의!)
# 파일이 존재하지 않으면 새로운 파일이 생성된다.
# 형식:
# 변수명 = open("파일명", "열기모드", 옵션)
# w: 쓰기 모드
# t: text 모드 (생략하면)
# b: binary 모드

# 1. 파일 열기
f = open(filename, "wt", encoding="utf-8")  # t 생략: text, encoding 생략: cp949

# 2. 파일 처리 (쓰기)
# 형식:
# 파일객체명.write("문자열")
# 파일객체명.write(변수)
# 리턴값: 파일에 쓴 문자열의 개수를 반환한다.
print(f.write("Hello"))  # 5

# 3. 파일 닫기
# 형식: 
# 파일변수명.close()
f.close()