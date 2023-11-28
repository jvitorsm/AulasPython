# Create a colection of elements from a iterable for which a function return true

# filter(function, itreable)
friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandeler", 21),
           ("Ross", 20)]

age = lambda data: data[1]>18

drinking_budies = list(filter(age,friends))

for i in drinking_budies:
    print(i)
