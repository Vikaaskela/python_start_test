#res = {}
#text = input('text=')
#for item in text:
#    if item not in res:
#        res[item] = text.count(item)
#print(res)

import operator

#print(operator.add(2, 3))
#print(operator.sub(5, 3))
#print(operator.truediv(2, 3))
#print(operator.mul(2, 3))

a, b = int(input('a=')), int(input('b='))
operation = input('operation')

calc = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,    
}

res = calc[operation] (a, b)
print(res)