#1
'''
print("Hello, World!")
'''
#2
'''
print(100+200)
'''
#3
'''
a , b ,c= map(int,input().split())
print(a+b+c)
'''

#4 복잡한 계산식
'''
print(1234*4321/5678)
'''

#5 문자열 길이 구하기 
'''
string = input()
lenght = len(string)
print(lenght)
'''

#6문자열 대소문자 변환
'''
string = input()
print(string.lower())
print(string.upper())
'''
#7문자열 포맷팅
'''
name = input('이름 = ')
age = int(input('나이 = '))
scnum = int(input('학번 = '))
print("내 이름은 %s, 그리고 나는 %d살 입니다. 학번은 %d 입니다."%(name,age,scnum))
print(f"내 이름은 {name}, 그리고 나는 {age}살 입니다. 학번은 {scnum} 입니다.")
'''

#8 문법 오류
printf("Hello, World!")