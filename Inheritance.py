# Inheritance its a concept where a  class can inherits something, usually attributes and methods
# of another class.

# Inheritance we create a relation of parent/child relationship where
# the child classes inherits the methods and attributes of parent class.
# In this example we created a class called Animal and another three classes
# (Rabbit, Fish and Hawk) where these will share what is inside Animal class

# Inheritance makes easier to do some global changes in the code.
# For example, if u have hundreds of classes, and you need to change
# the common function name attributed to all of them. Instead, to do
# this manually you can to change only in parent class and all the child
# class will inherited
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("This animal is running")

class Fish:

    def swim(self):
        print("This animal is swimming")

class Hawk(Animal):

    def fly(self):
        print("This animal is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()


# multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()