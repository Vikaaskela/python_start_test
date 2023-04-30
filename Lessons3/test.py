import random

x = [random.randrange(1,100) for _ in range(10)]

y = [item for item in x if item % 2]
z = [item for item in x if not item % 2]

print(x)
print(y)
print(z)
