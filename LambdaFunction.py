# lambda function = function in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x*2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age>= 1**-8 else False
print(double(5))
print(multiply(5,6))
print(add(7,58,9))
print(full_name('João','Vitor'))
print(age_check(18))

