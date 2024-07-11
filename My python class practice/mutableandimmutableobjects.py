name = 'blessing'
print(id(name))

name = name + ' ayo'
print(id(name))


number = 1
print(id(number))

number = number + 4 
print(id(number))
print(number)


basket = [1,2,3,4] 
print(id(basket))


basket.append(5)
print(id(basket))
print(basket) 



#strings are immutable object types, and such their addresses changes, but their object remain same
#int objects are also immutable 
# arrays objects are mutable(unchangeable) in their addresses but their object remain same
# append means to add a number to a set of variables 






