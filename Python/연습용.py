basket = ['apple', 'banana', 'kiwi']
if 'apple' in basket:
    pass
else:
    print("go to market")

print("이재진 바보")

a = 12818 / 3
b = 1234 * 4

if a > b: message = "a가 b보다 크다."
else: message = "b가 a보다 크다."
print(message)

message = "a가 b보다 크다." if a>b else "b가 a보다 크다."
print(message)

treehit = 0
while treehit < 10:
    treehit += 1
    print("나무를 %d번 찍었습니다." % treehit) 
    if treehit == 10:
        print("나무가 넘어갑니다.")


meal = 0
while meal < 3:
    meal += 1
    print(f"밥을 {meal}번 먹었습니다.")
else: print("배가 부릅니다.")

num = 1
while num <= 10: 
    print(num)
    num = num + 1 

height = 100
bounce = 3/5
number = 1
while number <= 10:
    number += 1
    height = height*bounce
    print(f'현재 {round(height,4)}만큼 높이에 있습니다.')



a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)


test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print(f'축하합니다. {number}번 학생은 합격하였습니다.')

add = 0
for i in range(1, 11):
    add += i
    print(add)