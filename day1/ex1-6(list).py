#리스트 []
# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

a = ['AB', 10, False]
x = a[1]        # a second
a[1] = 'Test'   # a second change
y = a[-1]       # a last element

x = a[1:3]      # [Test, False]
print(x)
print(a[:2])    # slice list[first index:last index]
print(a[3:])    # index begin(0), last element(index + 1)






