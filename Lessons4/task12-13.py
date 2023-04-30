#Task 12
#За допомогою циклів вивести на екран усі прості числа від 1 до 100.

for n in range(2, 100):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)