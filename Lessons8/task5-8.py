#Task 5
#Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
#> 123,34
#> one hundred twenty three dimport num2wordsollars thirty four cents
from num2words import num2words  


def func(x):
    a = num2words(int(x))
    v = (x - int(x))*100
    w = num2words(int(v))
    return f'{a}{" dollars and "}{w}{" cents"}'


m = float(input('x = '))
print(func(m))