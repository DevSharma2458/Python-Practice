def greetings_function():
    print("Hello, welcome to the Python learning session!")

greetings_function()

def name_function(name, age):
    print('Welcome ' +name+ ' You are ' +str(age)+ ' years old.')

name_function('Dev', 22)     

def name_function(name, age):
    print('Welcome ' +name+ ' You are ' +str(age)+ ' years old.')

name_function(name='Dev', age=22)

def name_function(name, age):
    print('Welcome ' +name+ ' You are ' +str(age)+ ' years old.')
name = input('Enter your name: ')
age = input('Enter your age: ')    
name_function(name='Dev', age=22)




def names(*names):
    print('Welcome '+names[1])
names('Dev', 'John', 'Alice') 













