# Duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attribute are preset
#               "if it walks like a duck, and it quacks like a duck, then it must be a duck


class Duck:
    def check(self):
        print("this is a Duck")

    def walk(self):
        print("This duck is walking like a duck")

    def talk(self):
        print("This duck is qwuacking like a duck")

class Chicken:
    def check(self):
        print("this is a chicken")

    def walk(self):
        print("This chicken is walking like a chiken")

    def talk(self):
        print("This chicken is clucking like a chiken")

class Person():

    def catch(self, animal):
        animal.walk()
        animal.talk()
        animal.check()
        #print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

person.catch(chicken)

