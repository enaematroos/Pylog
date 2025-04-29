# IF문

프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰는 것이 바로 if 문이다.

```python
>>> money = True
>>> if money:
...     print("택시를 타고 가라")
... else:
...     print("걸어 가라")
...
택시를 타고 가라
```
money에 True를 대입했으므로 money는 참이다. 따라서 if 문 다음 문장이 수행되어 '택시를 타고 가라'가 출력된다.

--- 

## if문의 기본 구조

if 조건문:
    수행할_문장1
    수행할_문장2
    ...
else:
    수행할_문장A
    수행할_문장B
    ...

조건문을 테스트해서 **참이면 if 문 바로 다음 문장(if 블록)들을 수행**하고 조건문이 **거짓이면 else 문 다음 문장(else 블록)들을 수행**하게 된다. 따라서 **else 문은 if 문 없이 독립적으로 사용할 수 없다.**

## 들여쓰기 (중요)

if 문을 만들 때는 if 조건문: 바로 다음 문장부터 if 문에 속하는 **모든 문장에 들여쓰기(indentation)를 해야 한다.**

*예시)*
if 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3

다음처럼 작성하면 오류가 발생한다. ‘수행할_문장2’를 들여쓰기하지 않았기 때문이다.

*오류가 발생하는 예시)*
if 조건문:
    수행할_문장1
수행할_문장2
    수행할_문장3

**즉, 들여쓰기는 언제나 같은 깊이로 해야 한다.**

***조건문 다음에 콜론(:)을 잊지 말자!***
**if 조건문 뒤에는 반드시 콜론(:)이 붙는다.** 앞으로 배울 while이나 for, def, class도 역시 문장의 끝에 콜론(:)이 항상 들어간다. 

---

## 조건문이란 무엇인가?

if 조건문에서 ‘조건문’이란 참과 거짓을 판단하는 문장을 말한다.

```python
>>> money = True
>>> if money:
```
money는 True이기 때문에 조건이 참이 되어 if 문 다음 문장을 수행한다.

## 비교연산자 (중요)

- x<y     x가 y보다 작다.
- x>y     x가 y보다 크다.
- x==y    x와 y가 같다.
- x!=y    x와 y가 같지 않다.
- x>=y    x가 y보다 크거나 같다.
- x<=y    x가 y보다 작거나 같다.

```python
x = 3
y = 2
print(x > y)
True
# x에 3, y에 2를 대입한 후 x > y라는 조건문을 수행하면 True를 리턴한다. x > y 조건문이 참이기 때문이다.

print(x < y)
False
# 위 조건문은 거짓이기 때문에 False를 리턴한다.

print(x == y)
False
# x와 y는 같지 않다. 따라서 위 조건문은 거짓이므로 False를 리턴한다.

money = 2000
if money >= 3000:
     print("택시를 타고 가라")
else:
     print("걸어가라")

걸어가라
```

## and, or, not

- x or y  x와 y 둘 중 하나만 참이어도 참이다.
- x and y x와 y 모두 참이어야 참이다.
- not x   x가 거짓이면 참이다.

```python
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
택시를 타고 가라
```
money는 2000이지만, card가 True이기 때문에 money >= 3000 or card 조건문이 참이 된다. 따라서 if 문에 속한 ‘택시를 타고 가라’ 문장이 출력된다.

## in, not in

- x in 리스트 (or not in 리스트) 리스트 안에 x이 있나? 없나?
- x in 튜플   (or not in 튜플)  튜플 안에 x가 있나? 없나?
- x in 문자열 (or not in 문자열) 문자열 안에 x가 있나? 없나?

```python
1 in [1, 2, 3]
True
1 not in [1, 2, 3]
False

'a' in ('a', 'b', 'c')
True

'j' not in 'python'
True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
택시를 타고 가라
```

## pass

**조건문에서 아무 일도 하지 않게 설정하고 싶다면** 
가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때나 아무런 일도 하지 않도록 설정하고 싶을 때가 있다.

*예시)*
```python
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
     pass 
else:
     print("카드를 꺼내라")
```

## 다양한 조건을 판단하는 elif

if와 else만으로는 다양한 조건을 판단하기 어렵다. elif라는 것을 사용하면 여러 개의 조건을 검사해서 그중에서 맘에 드는 것을 고를 수 있다.

*예시)*
```python
# if와 else만으로 '주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.'를 표현할 때

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")
택시를 타고 가라

# 이런 복잡함을 해결하기 위해 파이썬에서는 다중 조건 판단을 가능하게 하는 elif를 사용한다.

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
        print("걸어 가라")
택시를 타고 가라 
```

즉, **elif는 이전 조건문이 거짓일 때 수행된다.** if, elif, else를 모두 사용할 때 기본 구조는 다음과 같다.
```
if 조건문:
    수행할_문장1 
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
   수행할_문장1
   수행할_문장2
   ... 
```

## 조건부 표현식

조건부 표현식(conditional expression)을 사용하면 코드를 간단히 표현할 수 있다. 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.

*예시)*
```python
# 기본 if문 사용시
if score >= 60
    message = "success"
else:
    message = "failure"

# 조건부 표현식 사용시
message = "success" if score >= 60 else "failure"
```
조건부 표현식의 정의는 다음과 같다:
변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값

---

# while문

**문장을 반복해서 수행해야 할 경우 while 문을 사용한다.** 그래서 while 문을 ‘반복문’이라고도 부른다.

*예시)*
```
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
```

while 문은 **조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행**된다.

‘열 번 찍어 안 넘어가는 나무 없다’라는 속담을 파이썬 프로그램으로 만들면 다음과 같다.

```python
treehit = 0
while treehit < 10:
    treehit = treehit+1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무가 넘어갑니다.")

나무를 1번 찍었습니다.
나무를 2번 찍었습니다.
나무를 3번 찍었습니다.
나무를 4번 찍었습니다.
나무를 5번 찍었습니다.
나무를 6번 찍었습니다.
나무를 7번 찍었습니다.
나무를 8번 찍었습니다.
나무를 9번 찍었습니다.
나무를 10번 찍었습니다.
나무 넘어갑니다.
```
treeHit가 10보다 작은 동안 while 문에 포함된 문장들을 계속 수행한다. 그러고 나면 treeHit < 10 조건문이 거짓이 되므로 while 문을 빠져나가게 된다.

**treeHit 값을 1만큼씩 증가시킬 목적으로 사용하며 treeHit += 1처럼 작성해도 된다.**


## 강제로 while문에서 빠져나가기

```python
coffee = 10
money = 300
while money:
     print("돈을 받았으니 커피를 줍니다.")
     coffee = coffee -1
     print("남은 커피의 양은 %d개입니다." % coffee)
     if coffee == 0:
         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
         break

# 현실 자판기의 작동과정과 비슷하게 수정

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
```
money가 300으로 고정되어 있고 while money:에서 조건문인 money는 0이 아니기 때문에 항상 참이다. 따라서 무한히 반복되는 무한 루프를 돌게 된다. 그리고 while 문의 내용을 한 번 수행할 때마다 coffee = coffee - 1에 의해 coffee의 개수가 1개씩 줄어든다. 만약 coffee가 0이 되면 if coffee == 0: 문장에서 coffee == 0이 참이 되므로 if 문 다음 문장 "커피가 다 떨어졌습니다. 판매를 중지합니다."가 출력되고 break 문이 호출되어 while 문을 빠져나가게 된다.


## while문의 맨 처음으로 돌아가기

while 문 안의 문장을 수행할 때 입력 조건을 검사해서 조건에 맞지 않으면 while 문을 빠져나간다. 그런데 맨 처음(조건문)으로 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 이때 사용하는 것이 바로 continue 문이다.

*예시)*
```python
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)

1
3
5
7
9
```

## 무한루프

while 문의 조건문이 True이므로 항상 참이 된다. **따라서 while 문 안에 있는 문장들은 무한히 수행될 것이다.**

*예시)*
```python
while True:
     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
```

---

# for문

for 문의 기본 구조는 다음과 같다.
```
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
    ...
```

리스트나 튜플, 문자열의 **첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입**되어 ‘수행할_문장1’, ‘수행할_문장2’ 등이 수행된다.


1. 전형적인 for문
```python
test_list = ['one','two','three']
for i in test_list:
    print(i)

one
two
three
```
리스트의 첫 번째 요소인 'one'이 먼저 i 변수에 대입된 후 print(i) 문장을 수행한다. 다음에 두 번째 요소 'two'가 i 변수에 대입된 후 print(i) 문장을 수행하고 리스트의 마지막 요소까지 이것을 반복한다.

2. 다양한 for문의 사용

```python
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

3
7
11
```
위 예는 a 리스트의 요솟값이 튜플이기 때문에 각각의 요소가 자동으로 (first, last) 변수에 대입된다.

3. for문의 응용

```
총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.
```

위 문제를 for문을 응용하여 만들면 다음과 같다.

```python
marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트

number = # 학생에게 붙여 줄 번호
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

1번 학생은 합격입니다.
2번 학생은 불합격입니다.
3번 학생은 합격입니다.
4번 학생은 불합격입니다.
5번 학생은 합격입니다.
```

## for문과 continue문

while 문에서 살펴본 continue 문을 for 문에서도 사용할 수 있다. 즉, for 문 안의 문장을 수행하는 도중 continue 문을 만나면 for 문의 처음으로 돌아가게 된다.

```python
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue # 조건에 맞으면 number이 +1된 채로 for문의 처음으로 돌아감 
    print(f'축하합니다. {number}번 학생은 합격하였습니다.')

축하합니다. 1번 학생은 합격하였습니다.
축하합니다. 3번 학생은 합격하였습니다.
축하합니다. 5번 학생은 합격하였습니다.
```

## for과 함께 자주 사용하는 range 함수
for 문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많다. 다음은 range 함수의 간단한 사용법이다.
```
>>> a = range(10)
>>> a
range(0, 10)
```

*예시)*
```python
add = 0
for i in range(1, 11)
    add += 1
    print(add)
```
range(1, 11)은 숫자 1부터 10까지(1 이상 11 미만)의 숫자를 데이터로 가지는 객체이다. 따라서 위 예에서 **i 변수에 숫자가 1부터 10까지 하나씩 차례로 대입되면서 add = add + i 문장을 반복적으로 수행하고 add는 최종적으로 55가 된다.**

