#Task 7
#Є список [0, 5, 2, 4, 7, 1, 3, 19].
#Напишіть скрипт для підрахунку непарних цифр у ньому.

#x = [0, 5, 2, 4, 7, 1, 3, 19]
#import random
#y = [item for item in x if  item % 2]
#print(y)

#x = [0, 5, 2, 4, 7, 1, 3, 19]
#count = 0
#for item in x:
#    if item % 2:
#        count += 1
#print(count)

x = [0, 5, 2, 4, 7, 1, 3, 19]
print(len([item for item in x if item % 2]))