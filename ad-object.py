class Student(object):
    pass

s = Student()
s.name = 'Micheal'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)

s2 = Student()

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(88)
print(s2.score)

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Micheal'
s.age = 25
# s.score = 99
# 由于'score'没有被放到__slots__中
# 所以不能绑定score属性
# 试图绑定score将得到AttributeError的错误。
# __slots__定义的属性仅对当前类实例起作用
# 对继承的子类是不起作用的


class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value >100:
            raise ValueError('score must be inside 0~100')
        self._socre = value

s = Student()
s.set_score(59)
print(s.get_score)


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()

s.score = 80
print(s.score)


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        self._resolution = self._height * self._width
        return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


