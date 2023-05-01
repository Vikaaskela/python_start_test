#Task 1
#Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. 
#Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
def func (seq, x):
    """ 
    Searching for an element in a list of integers
    Args:
        seq (list): list of integers
        x (number): number of compare

    Returns:
        index: if not, then return the number "-1"
    """
    return f'{seq.index(x) if x in seq else "-1"}'
print(func([1,2,3,4,5], 7))

