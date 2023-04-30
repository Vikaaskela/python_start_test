#Task 11
#Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
#Список може бути довільною довжиною.

x = [2, 5, 9, 3]
x.reverse()
print(x)

print(x[::-1])
print(x)

for item in reversed(x):
    print(item)
print(x)