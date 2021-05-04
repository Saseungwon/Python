# 연산자 오버로딩
class NumBox:
    def __init__(self, num):
        self.Num - num

    def __add__(self, num):
        self.Num += num

    def __sub__(self, num):
        self.Num -= num

    def __del__(self):
        print('소멸되었습니다.')

n = NumBox(10)
n + 100
print(n.Num)
n - 110