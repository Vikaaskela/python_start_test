#Task 9
#Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць. 
#Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

#import random
#x = [random.randrange(10000, 15000) for i in range(12)]
#print(x)
#res = sum(x) // len(x)
#print(res)

import random
salary = [random.randint(10_000, 100_000) for _ in range(12)]
print(sum(salary) / len(salary))