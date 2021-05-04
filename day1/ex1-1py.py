import math
print(math.sqrt(9.8))  #주석처리!!!
#주석처리!!!

#변수
a = 123
print(type(a))
b = '승원'
print(type(b))
c = [1,2,3,4,5]
print(type(c))

# 문자열
d = """띄어쓰기 해도 붙여서 나온다. ㅋ ㅋ ㅋ  ㅋ ㅋ ㅋ
asdf
asd
f
a
sdf
asdf
sadf"""
print(d)

#문자열 곱하기 가능
print('=' *50)

print(b[0])
print(b.count('승'))

g = 'abcdefg ab aaa'
print(g.count('a'))
print(b.find('원'))

f=','
print(f.join('abcd'))

d = input('입력해주세요 : ')
print(d)



#console
#3.1304951684997055
#<class 'int'>
#<class 'str'>
#<class 'list'>
#띄어쓰기 해도 붙여서 나온다. ㅋ ㅋ ㅋ  ㅋ ㅋ ㅋ
#asdf
#asd
#f
#a
#sdf
#asdf
#sadf
#==================================================
#승
#1
#5
#1
#a,b,c,d
#입력해주세요 : >? ipruk input hhh
#ipruk input hhh