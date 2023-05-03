#Task 1
#Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. 
#Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
'''
def func (seq, x):
    """ 
    Searching for an element in a list of integers
    Args:
        seq (list): list of integers
        x (number): number of compare

    Returns:
        index: if not, then return the number "-1"
    """
    return seq.index(x) if x in seq else "-1"
print(func([1,2,3,4,5], 7))
'''
import random


def search_index(sequence, item):
    for index, element in enumerate(sequence):
        if element == item:
            return index
    return -1


seq = [random.randint(0, 50) for _ in range(20)]
item = int(input('item='))
res = search_index(seq, item)
if res == -1:
    print('No Item')
else:
    print(f'Index of Item = {res}')
