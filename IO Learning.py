f = open('/Users/djc19/test/test.txt', 'r')
print(f.read())
f.close()

with open('/Users/djc19/test/test.txt', 'r') as f:
    print(f.read())

# f = open('/Users/djc19/test/test.jpg', 'rb')
# print(f.read())

f = open('/Users/djc19/test/test.txt', 'w')
f.write('Stupid man')
f.close()

from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('World'))
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())


import os
print(os.name)

print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join('/Users/djc19/test', 'testdir'))
# os.mkdir('/Users/djc19/test/testdir')
# os.rmdir('/Users/djc19/testdir')


import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

import json

d = dict(name='Micheal', age=11, score=61)
print(json.dumps(d))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score':std.score
    }

s = Student('Cathy', 32, 99)
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))
# 通常class的实例都有一个__dict__属性
# 它就是一个dict，用来存储实例变量
# 也有少数例外，比如定义了__slots__的class。

obj = dict(name='大姚', age=20)
s1 = json.dumps(obj, ensure_ascii=True)
print(s1)
s2 = json.dumps(obj, ensure_ascii=False)
print(s2)