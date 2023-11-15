# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more methods.
# abstract method = a method that has a declaration but does not have an implemantation

from abc import  ABC, abstractmethod

class Vehichle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehichle):

    def go(self):
        print("You drive the car")


    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehichle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehichle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
