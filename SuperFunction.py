# super() = Function used to give access to methods of a parent class
#            Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.lenght = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        #self.length = length
        #self.width = width
        super().__init__(length,width)

    def area(self):
        return self.lenght*self.width

class Cube(Rectangle):

    def __init__(self,length, width, height):
        #self.lenght = length
        #self.width = width
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.lenght*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())

