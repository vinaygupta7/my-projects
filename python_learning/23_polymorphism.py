class Animal():
    def __init(self,name):
        self.name=name
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print('Meow!')

class Dog(Animal):
    def talk(self):
        print("Bark!")

c=Cat()
c.talk()

d=Dog()
d.talk()
