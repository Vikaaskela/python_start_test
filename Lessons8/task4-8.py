#Task 4
#Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
#Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99. 
#Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел. 
#Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.
def func():
    """ Find the largest palindrome obtained by multiplying two three-digit numbers.
    """
    x=[]
    for i in range(100, 1000):
        for j in range(100, 1000):
            a = str(i * j) 
            if a == a[::-1]:
                x.append(int(a))
    print(max(x)) 
func()