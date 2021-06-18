class Animal():
    def __init__(self, breed, owner):
        print('CLASS ANIMAL CREATED')
        self.breed = breed
        self.owner = owner

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am Eating')


class Tech():
    def __init__(self, name):
        print('CLASS TECH CREATED')
        self.name = name


class Dog(Animal):

    def __init__(self, breed, owner):
        super().__init__(breed, owner)
        print('dog created')

    def who_am_i(self):
        print('I am a dog!')
        print(self.breed)
        print(self.owner)


class Mobile(Tech):

    def __init__(self, name):
        super().__init__(name)

    def who_am_i(self):
        print('Helo')
        print(self.name)


my_dog = Dog('golden retriever', 'ayush')
my_dog.who_am_i()

my_mobile = Mobile('samsung')
