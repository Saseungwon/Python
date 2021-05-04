# 상속
class Animal:
    def __init__(self, name):
        self.name = name
        def move(self):

class Dog(Animal):
    def speak(self):
        print('bark')
class Duck(Animal):
    def speak(self):
        print('quack')

dog = Dog('doggy') #
n = dog.name        # 부모 클래스의 인스턴스 변수
print(n)
dog.move() # 부모 클래스의 메서드
dog.speak()
duck = Duck('ducks')
print(duck.name)