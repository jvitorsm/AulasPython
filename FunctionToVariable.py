def hello():
    print("Hello")

hello()

print(hello)    # print the memory address of the function that is located in the memory of the computer (hexdecimal)

hi = hello      # without the set of parentheses cause the set would be calling the function hello()
                #   and returnig the name to hi

print(hi)       # when you attribute a variable to the name of a function those to information it will have the same me
                #   memory address, that means they gonna storage the same information.
hi()
hello()

say = print
say("Whoa that worked :o")


