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
del s.name
print(s.name)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')


# 我来解释下这段代码为什么不行：

# class Student(object):
#    count = 0
#
#   def __init__(self, name):
#        self.name = name
#        self.count += 1  # 错误
#
# s1 = Student('A')
# 首先，在 Python 中任何数据都是对象，包括 0，1 这样的数字。
#
# count = 0 为类和实例都添加了 count 属性，并将这属性指向 0 这个对象，即：
#
# Student.count ===> 0
# s1.count ===> 0
# self.count += 1 即 self.count = self.count + 1，但是由于 int 类型是不可变的，Python 只能将 self.count 指向一个新的对象 1，而不是去修改 self.count 所指向的对象。
#
# 那么这行代码执行完后：
#
# Student.count ===> 0  # 没有被修改，依旧为 0
# s1.count ===> 1  # 指向了新的对象 1
# 所以这里你只能写成 Student.count += 1。