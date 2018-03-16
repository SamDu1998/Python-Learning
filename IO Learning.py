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
f.write('hello')
