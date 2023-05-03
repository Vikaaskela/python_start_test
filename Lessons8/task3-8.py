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
def is_arithmetic(sequence):
    if len(sequence) <= 2:
        return False

    d = sequence[1] - sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != d:
            return False

    return True


def get_next_number_arithmetic(sequence):
    if len(sequence) <= 2:
        return None
    d = sequence[1] - sequence[0]
    return sequence[-1] + d


def is_geometric(sequence):
    if len(sequence) <= 2:
        return False

    p = sequence[1] / sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] / sequence[i] != p:
            return False

    return True


def get_next_number_geometric(sequence):
    if len(sequence) <= 2:
        return None
    p = sequence[1] / sequence[0]
    return sequence[-1] * p


def get_number(sequence):
    if is_arithmetic(sequence):
        return get_next_number_arithmetic(sequence) 
    if is_geometric(sequence):
        return get_next_number_geometric(sequence)


x = [1,2,4,8,16,32,64]
print(get_number(x))