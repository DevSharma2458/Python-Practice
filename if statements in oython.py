a = 4
b = 3
if a > b:
    print(str(a) + " is greater than " + str(b))
elif a < b:
    print(str(a) + " is less than " + str(b))
else:
    print(str(a) + " is equal to " + str(b))

 #print(a + " is greater than " + b) This won't work

a1 = 5
b1 = 7
if a1 == b1:
    print('a1 = b1')

# yaha ye string he return karega kyuki value input () hamesha string he leta hai
value = input('Input a value: ')

if type(value) is int:
    print('The value is an integer')
elif type(value) is str:
    print('The value is a string')
elif type(value) is list:
    print('The value is a list')
else:
    print('We don\'t know the data type of' , value)    


value = int(input('Input a value: '))

if type(value) == str:
    print('The value is a string')
else:
    print(value, 'is not a string')    




value = int(input('Input a value: '))

if value%5 == 0:
    print(value, 'can be divided by 5')
else:
    print(value, 'cannot be divided by 5') 



# it will not work
value = input('Input a value: ')

if value<10:
    print(value, 'is less than 10')
else:
    print(value, 'is more than 10') 

















