'''
def func(*args, op = '+'):
    if op == '+':
        s = 0
        for item in args:
            if isinstance(item, int) and item % 2 ==0:
                s += item
        return s
    if op == '*':
        s = 1
        for item in args:
            if isinstance(item, int) and item % 2 ==0:
                s *= item
        return s
print(func(1, 1, 2, 3, 4, 5, 5, op='+'))
'''
'''
def func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
print(func(a=2, b=3, c=4))
'''
'''
def func(a, b, *args,**kwargs):
    s = a + b
    for item in args:
        s += item
    return s
print(func(1, 2))

print(func(1, 2, 3))
'''
'''
def my_double_add(a, b):
    a *= 2
    b *= 2
    return a + b
a = 2
b = 4
print(my_double_add(a, b))
print(a)
print(b)
'''
'''
def my_double_add(x):
    x.append(20)
    print(x)
a =[10, 20, 30]
my_double_add(a[:])
my_double_add(a[:])
my_double_add(a[:])
print(a)
'''
'''
def my_double_add(x=None):
    if not x:
        x = []
    x.append(20)
    print(x)

my_double_add()
my_double_add()
my_double_add()
'''
'''
x = 10

def func():
    y = 20
    def inner():
        nonlocal y
        y = 40
        z = 30
        x = 1
        res = x + y + z
        return res
    return inner() + y
print(func())
'''
def punk(l):
    return zip(l[:-2], l[1:-1], l[2:])
print(punk([1,5,9,13,17]))