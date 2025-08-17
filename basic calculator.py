'''num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator (+, -, *, /, %): ')

if op == '+':
    print('The result is:', num1 + num2)
elif op == '-':
    print('The result is:', num1 - num2)
elif op == '*':
    print('The result is:', num1 * num2)
elif op == '/':
    print('The result is:', abs(num1 / num2))
elif op == '%':
    print('The result is:', abs(num1 % num2))
else:
    print('Invalid operator')'''



'''Basic Calculator ''' 
num1_input = input('Enter first number: ')
if num1_input.isdigit():
    num1 = float(num1_input)
else:
    print('❌ Please enter a valid number')
    exit()

num2_input = input('Enter second number: ')
if num2_input.isdigit():
    num2 = float(num2_input)
else:
    print('❌ Please enter a valid number')
    exit()

op = input('Enter operator (+, -, *, /, %): ')

if op == '+':
    print('The result is:', num1 + num2)
elif op == '-':
    print('The result is:', num1 - num2)
elif op == '*':
    print('The result is:', num1 * num2)
elif op == '/':
    if num2 == 0:
        print('❌ Cannot divide by zero')
    elif num1 == 0:
        print('❌ Cannot divide by zero')
    else:
        print('The result is:', abs(num1 / num2))
elif op == '%':
    if num2 == 0:
        print('❌ Cannot modulo by zero')
    elif num1 == 0:
        print('❌ Cannot modulo by zero')
    else:
        print('The result is:', abs(num1 % num2))
else:
    print('❌ Invalid operator')



















