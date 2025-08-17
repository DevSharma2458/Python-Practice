for letter in 'Python':
    print(letter)

fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit)

for char in "hello":
    print(char)

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
    print(i, color)


data = {"name": "Dev", "age": 22}
for key, value in data.items():
    print(key, value)


for i in range(i<=3):
    for j in range(2):
        print(i, j)


mylist = [1, 2,'ji', 'ju', 'jo']
for item in mylist:
    print(item)



mylist = [1, 2,'ji', 'ju', 'jo']
for item in mylist:
    if item == 'ji':
        break
    print(item)


for x in range (1, 22):
    if x % 2 == 0:
        continue
    print(x)

    
for x in range (7):
    print(x)
else:
    print("Loop completed")
