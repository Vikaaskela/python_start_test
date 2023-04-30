#Task 1
#Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.
#Створіть список із числами, які є в обох списках.

import random

x = {random.randrange(1, 100) for item in range(20)}
y = {item for item  in x if item % 3 == 0}
z = {item for item  in x if item % 5 == 0}
print(x, y, z)
print(set.intersection(y, z))


