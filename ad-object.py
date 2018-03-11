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


# 多重继承

class Animal(object):
    pass

# 大分类
class Mammals(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running')

class FlyableMixIn(object):
    def fly(self):
        print('Flying')


# 各种动物

class Dog(Mammals, RunnableMixIn):
    pass

class Bat(Mammals, FlyableMixIn):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

d = Dog()
print(d.run())

# 定制类

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__

print(Student('Micheal'))
Student('Micheal')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)


# __Getitem__

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a,b = b, a+b
        return a

f = Fib()

print(f[0])
print(f[10])
print(f[100])

# 对于Fib却报错
# 原因是__getitem__()传入的参数可能是一个int
# 也可能是一个切片对象slice，所以要做判断：

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f[0:5])


# __getattr__

class Student(object):

    def __init__(self):
        self.name = 'Micheal'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

        if attr == 'age':
            return lambda: 25

s = Student()
print(s.score)
print(s.age())
print(s.width)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)


# __call__

class Student():
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Micheal')
print(s())


# 使用枚举类

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Thu)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


# 使用元类

def fn(self, name='world'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
print(h.hello())
print(type(h))

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name,bases, attrs)

class MyList(list, metaclass=ListMetaclass):
        pass

L = MyList()
L.add(1)
print(L)




class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

     def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100')

class IntegerField(Field):
     def __init__(self, name):
         super(IntegerField, self).__init__(name, 'bright')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases,attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))



class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 当用户定义一个class User(Model)时
# Python解释器首先在当前类User的定义中查找metaclass
# 如果没有找到，就继续在父类Model中查找metaclass
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

# 在ModelMetaclass中，一共做了几件事情：

# 排除掉对Model类的修改；

# 在当前类（比如User）中查找定义的类的所有属性
# 如果找到一个Field属性
# 就把它保存到一个__mappings__的dict中
# 同时从类属性中删除该Field属性
# 否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

# 把表名保存到__table__中，这里简化为表名默认为类名。

# 在Model类中,就可以定义各种操作数据库的方法
# 比如save()，delete()，find()，update等等。

# 我们实现了save()方法，把一个实例保存到数据库中
# 因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。

u = User(id=12345, name='Micheal', email='test@sustc.educ.com', password='my-pwd')
u.save()