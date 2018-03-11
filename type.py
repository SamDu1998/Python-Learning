print(type(123))

import types

def fn():
    pass

print(type(fn) == types.FunctionType)

class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))

print(dir('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()

print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)

setattr(obj, 'y', 19)

print(obj.y)

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Micheal'
print(s.name)
