#Task 2
#Реалізуйте функцію, параметрами якої є два числа та рядок. 
#Повертає вона конкатенацію рядка із сумою чисел.

#x = int(input('x='))
#y = int(input('y='))
#def func(x, y, k = 'Hello'):
#    return 'Hello ' + str(x + y)
#print(func(x, y, 'Hello'))

def myfunc(num1, num2, user_str):
    '''
    
    
    '''
    
    return f'{user_str} {num1 + num2}'

print(myfunc(10, 20, 'hello'))