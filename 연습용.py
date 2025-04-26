# 딕셔너리 자료형 

ball = {
    "baseball": "야구",
    "soccer": "축구",
    "basketball": "농구"
}
print(ball["basketball"])

fruit = {"apple":"red"}
fruit = {"banana":"yellow"}
print(fruit) # 대체됨

fruit["apple"] = "red"
fruit["banana"] = "yelloew"
fruit["grape"] = "purple"
print(fruit)
# {'banana': 'yelloew', 'apple': 'red', 'grape': 'purple'}

a = {
    '성수':'바보',
    '코비':'귀여버',
    '성민':'이뽀'
}

a['아빠']='짜증냄'

dic = {
    'you':'me',
    'dont':'call',
    'pay':'phone'
}
print(dic.keys())
print(dic.items())
print(dic.clear())

dic = {
    'you':'me',
    'dont':'call',
    'pay':'phone'
}

print(dic.get('you'))
print(a.get('I','없음'))

print('you' in dic)

집합 = set([1, 2, 3])
print(집합)

s2 = {'바', '나', '나', '맛', '있', '다'}
print(s2)

s1 = {1,2,3}
s2={2,3,4}

print(s1&s2)
print(s1|s2)
print(s1-s2)
print(s2-s1)

s1.update([4])
print(s1)

s1.remove(4)
print(s1)

print(2>1)