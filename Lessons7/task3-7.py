#Task 3
#Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». 
#Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
'''
def draw_rectangle(m: int, n: int):
    return  f"{'*' * n}\n" + (m - 2) * f"*{' ' * (n - 2)}*\n" + f"{'*' * n}\n"
    print('*' * n)
    for i in range(m-2):
        print('*', ' ' * (n - 2), '*', sep=' ')
    print('*' * n) 

draw_rectangle(6,7)   
'''
def draw_rectangle(m: int, n: int):
    return  f"{'*' * n}\n" + (m - 2) * f"*{' ' * (n - 2)}*\n" + f"{'*' * n}\n"
print(draw_rectangle(6,7) )