#Task 3
#Існують такі послідовності чисел:
#0,2,4,6,8,10,12
#1,4,7,10,13
#1,2,4,8,16,32
#1,3,9,27
#1,4,9,16,25
#1,8,27,64,125
#Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
#Послідовність користувач вводить з клавіатури у вигляді рядка. 
#Наприклад, користувач вводить рядок 0,5,10,15,20,25 та відповіддю програми має бути число 30.
def func(*args):
    """ Write a program that outputs the next member of this sequence

    Returns:
        number: the next member of this sequence
    """
    #if args[3] - args[2] == args[2] - args[1]:
    #    return args[-1] + (args[2] - args[1])
    #if args[3] / args[2] == args[2] / args[1]:
    #    return args[-1] * (args[2] / args[1])
    return f'{args[-1] + (args[2] - args[1]) if args[3] - args[2] == args[2] - args[1] else args[-1] * (args[2] / args[1])}'
print(func(1,3,9,27))