class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())