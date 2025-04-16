palindrom = "스위스토마토기러기오디오"
print(palindrom[::-1])
# 거꾸로 읽어도 같은지 검사하는 코드

#문자열 포매팅 : 일정한 문자열을 정해두고(포맷), 포맷 안의 특정 숫자나 문자만 바꿀 때
a = "I eat %d apples." % 3
print(a)
b = "I eat %s apples." % "five" # % s는 무슨 값이든 상관 x % s만 알아도 상관 x
print(b)
number = 3
a = "I eat %d apples." % number
print(a)

# 한번에 두 가지 변수 넣는 문자열 포매팅
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

# 문자열 포매팅에 문자 '%' 자체를 넣고 싶을 때 -> %% 쓰기
a = "I eat %s%% apples from basket" % 3
print(a)
b = "error is %s%% percent." % 98
print(b)

# 거의 안쓰는... 문자&숫자 포매팅
a = "%10s" % "hi" # 10글자자리에 hi(2글자) 맨 뒤로 삽입
print(a)
b = "%-10s" % "hi" # 10글자자리에 hi(2글자) 맨 앞으로 삽입
print(b)

# 문자열 포매팅을 사용해서 숫자의 소수점 표현하기
a = "%0.3f" % 3.241592 # 소수점 3자리만 표현(%.3f도 가능)
print(a)
b = "%10.3f" % 3.241592
print(b)

# 또다른 포매팅 방법
a = "I eat {0} apples" .format(3) #문자 넣을 땐 괄호 안에 ("three")
print(a)
b = "I ate {0} apples. so I was sick for {1} days." .format(3, "two") # 인덱스 {0},{1} 자리 확인
print(b)
c = "I ate {number} apples. so I was sick for {day} days." .format(number=3, day = "two")
print(c)

# 정렬 (많이 쓰이지는 x)
a = "{0:<10} World" .format("hi") # 왼쪽 정렬
print(a)
a = "{0:>10} World" .format("hi") # 오른쪽 정렬
print(a)
a = "{0:^10} World" .format("hi") # 가운데 정렬
print(a)
a = "{0:=^10} World" .format("hi") # 공백 채우기
print(a)
a = "{0:!<10} World" .format("hi") # 공백 채우기
print(a)
y = 3.42134234
a = "{0:0.4f}" .format(y) # 소수점 넷째자리까지 표현
print(a)

# f 문자열 포매팅 (요즘 가장 많이 쓰임)

name = "홍길동"
age = 30
a = f"나의 이름은 {name}입니다. 나이는 {age}입니다" # 작은따옴표도 가능
print(a)
age = 30
a = f'내년에는 {age+1}살이 됩니다.' # 변수 계산도 가능, 정렬도 위랑 똑같음
print(a)

# 소수점 표현하기
y = 3.241234
a = f'{y:0.3f}'
print(a)

# 중괄호 표현하기
a = f'{{and}}'
print(a)

number = 1234567890
formatted_number = f"{number:,}"
print(formatted_number)