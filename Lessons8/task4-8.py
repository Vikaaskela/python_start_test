#Task 4
#Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
#Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99. 
#Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел. 
#Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.
def func(start, stop):
    """ Find the largest palindrome obtained by multiplying two three-digit numbers
    """
    x=[]
    for i in range(start, stop):
        for j in range(start, stop):
            a = str(i * j) 
            if a == a[::-1]:
                x.append(int(a))
    return max(x) 
print(func(start, stop))

def palindrom_2(start: int, stop: int):
    max_item = 0
    for i in range(start, stop):
        for j in range(start, stop):
            res = str(i * j) 
            if res == res[::-1] and int(res) > max_item:
                max_item = int(res)
    return max_item 
print(func(100, 1000))
print(palindrom_2(100, 1000))