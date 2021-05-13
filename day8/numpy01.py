import numpy as np           ## 다차원 배열의 모듈을 import 한다. 모듈의 별칭은 np를 사용한다.



a = np.array([1,2,3,4])           ## array 함수에 4개의 원소를 가진 리스트를 전달해서 다차원 배열을 하나 만든다.

print(a.dtype)
print(a.shape)

print(a.ndim, a.shape, a.itemsize)           ## 다차원 배열은 차원, 형상, 하나의 원소의 바이트크기를 속성으로 관리한다


b = np.array([1,1,1,9])     ## 다른 다차원 배열을 하나 만든다.
c = a + b

print(c)

data1 = [1,2,3,4,5]
# numpy를 이용하여 array 정의하기
# 1. 위에서 만든 python list를 이용
arr1 = np.array(data1)

print(arr1)

arr4 = np.array([[1,2,3,4],[4,5,6,5]])
print(arr4.shape)
print(arr4.ndim, arr4.shape, arr4.itemsize)

# http://taewan.kim/post/numpy_cheat_sheet/




