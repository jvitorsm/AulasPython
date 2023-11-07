# walrus operator :=

#   new to python 3.8
#   assignment expression aka walrus operator
#   assigns values to variables as part of larger expression

#mood = "Happy"
#print(mood)

#print(mood:='Happy')


#   foodds = lists()
#   while True:
#       food = input("What food do you like?: ")
#           if food == "quit":
#               break
#       foods.append(food)

foods = []
while food := input("What food do would you like?: ") != "quit":
    foods.append(food)

# The walrus operator storage the data in booleans, so if you try to print a list 
#   build by walrus like in this example, the program shall return boolens.

for food in foods:
    print(food)
    