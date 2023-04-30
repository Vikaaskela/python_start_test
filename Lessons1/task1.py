print("Вітаю!")
a, b, c, d, e = int(input('a ')), \
                int(input('b ')), \
                int(input('c ')), \
                int(input('d ')), \
                int(input('e '))
                
print(f'Max={max(a, b, c, d, e)}')
print(f'Min={min(a, b, c, d, e)}')
print(f'Avg={(a + b + c + d + e) / 5}')