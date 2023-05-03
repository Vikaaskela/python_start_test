#Task 6
#Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
#Наприклад: XXII -> 22
#Докладніше: https://en.wikipedia.org/wiki/Roman_numerals
def func(rom):
    romans = {'I':1,
              'II':2,
              'III':3,
              'IV':4,
              'V':5,
              'VI':6,
              'VII':7,
             'VIII':8,
             'IX':9,
             'X':10,
    }
    x = []
    if 'IV' in rom:
        x.append(rom)
    for i in range(len(rom)):
        x.append(romans[rom[0+i]])

    return sum(x)

print(func("XX"))