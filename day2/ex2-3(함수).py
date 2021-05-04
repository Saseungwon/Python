#함수

# -*- coding: utf-8 -*-
def fn_name():
    print('안녕')


def fn_return():
    return 'hi', 1, [1,2,3]
a, b, c = fn_return() # 리턴 여러 개 가능
print(a, str(b), c)

d= fn_return() #한 개로 받으면 tuple형태로 리턴
for i in d:
    print(i)