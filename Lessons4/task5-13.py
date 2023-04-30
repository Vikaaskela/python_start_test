#Task 5
#Напишіть скрипт, який виводить на екран таблицю множення на 5. 
#Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...

#for i in range(1, 10): 
#    print(i, '*', 5, '=', 5*i)

#for i in range(1, 11):
#    print(f'1 x {i} == {i * 5}')

for j in range(1, 11):
    for i in range(1, 11):
        print(f'{j} x {i} == {i * j}')
    print('*' * 20)