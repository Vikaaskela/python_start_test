#Task 8
#Створіть список випадкових чисел (розміром 4 елементи).
#Створіть другий список у два рази більше першого, де перші 4 елементи 
#повинні дорівнювати елементам першого списку, а решта елементів - подвоєним значенням початкових.
#Наприклад,Було → [1,4,7,2]Стало → [1,4,7,2,2,8,14,4]

import random
x = [random.randint(1,100) for i in range(4)]
y = x+[item*2 for item in x] 
print(x)
print(y)