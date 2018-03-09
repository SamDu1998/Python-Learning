std1 = {'name': 'Micheal', 'socre': 98}
std2 = {'name': 'Bob', 'socre': 81}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_socre(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Invalid Socre')
        

bart = Student('Bart Simpon', 99)
bart.print_socre()

