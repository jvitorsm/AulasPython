from ClassVariableCar import Car

car_1 = Car("Chevy","Corvette",2021,"Blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.wheels = 2

print(f'Número de rodas: {car_1.wheels}')
print(f'Número de rodas: {car_2.wheels}')

#Intance variable its a variable that counts only for the instance of a function
#The class variable its a variable that affect all instance of a class
# In this example we have a class named "Car" that have the class variable: "Wheels"
# The instances variables its the value attributed to a make, model, year an dcolor of each car
#If you want to chanege the a class variable value on the main file you must wrhite:
# the name of the class captalized dot name of the variable and the equals sign and the value the you want.
# Ex.: Car.wheels = 2