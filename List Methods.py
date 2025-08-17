list1 = [1, 0, 4, 9, 8]
list2 = ['banana', 'apple','apple', 'orange', 'grape', 'kiwi', 'mango']

list1.extend(list2)
list2.append('pear')
list2.insert(2, 'peach')
list2.remove('kiwi')
list2.pop()
del list2[0]

print(list1)
print(list2)

print(list2.index('mango'))
print(list2.count('apple'))

list2.clear()
print(list2)

list1.sort()
print(list1)

list2.reverse()
print(list2)

list3 = list1.copy()
print(list3)



