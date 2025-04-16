# 숫자형 자료형 공식

# if a = 123, print(type(a)) = int
# if a = -2.84, print(type(a)) = float
# if a = 3 and b = 4, 
# print(a+b) = 7, print(a-b) = -1 
# print(a*b) = 12, print(a/b) = 4/3
# print(a**b) = 81 연산자
# print(7//3) = 2 몫, print(7 % 3) = 1 나머지


# 문자열 자료형 공식

a = "life is too short, you need python"
# print(type(a)) = str
# 큰따옴표, 작은따옴표 양쪽 1개, 3개로 감싸 문자열 만들기
# ex) "HELLO" """HELLO""" 'HELLO' '''HELLO'''
# 백슬래쉬(\)를 쓰면 뒷문자를 보전할 수 있음 ex)Life\" = life"
# 줄바꿈(\n) ex) """Life is short, \nYou need python"""
# 문자열 사이 탭 간격 줄 때 (\t) 

head = "python"
tail = "\tis fun!"
print(head+tail)
# = python  is fun!
print(head*3)
# = pythonpythonpython 참고* = 문자열끼리 곱할 수는 x

print("=" * 50) 
print("My Program")
print("=" * 50)
# ==================================================
# My Program 문자열 곱하기 응용 ㅎ0ㅎ
# ==================================================

a = "life is too short, you need python"
print(len(a)) # = 34 문자열의 길이 구하기(인덱싱)
print(a[3]) # = e 인덱스(몇번째에 무슨 문자열인지)
# 참고* 파이썽의 인덱스는 0번부터 시작이라 3번 인덱스가 e임

print(a[0]) # = l
print(a[12]) # = s
print(a[-1]) # = n 참고* 음수는 거꾸로 간다
b = a[0:4] # ~이상 ~미만 ~간격으로 가져옴 (0,1,2,3)
print(b) # = life
print(a[19: ]) # = you need python 비워둘 수도 o
print(a[::2]) # = lf stosot o edpto 간격
print(a[::-1]) # = nohtyp deen uoy ,trohs oot si efil

#응용연습 해보기 
weather = "20250410rainy"
print(len(weather)) # = 13
print(weather[:8]) # = 20250410
print(weather[8:]) # = rainy
month = weather[4:6]
day = weather[6:8]
print(month+day)