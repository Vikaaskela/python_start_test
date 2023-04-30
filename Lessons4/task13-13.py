#Task 13
#Виведіть на екран «пісочний годинник», максимальна ширина якого зчитується 
#з клавіатури (число непарне). У прикладі ширина дорівнює 5.
#*****
# ***
#  *
# ***
#*****

#n = int(input('stars='))
#spaces = 0
#for i in range(n, 0, -2):
#    print(f"{' ' * spaces}{'*' * i}")
#    spaces += 1

n = int(input('stars='))
spaces = 0
lines = []
for i in range(n, 0, -2):
    lines.append(f"{' ' * spaces}{'*' * i}")
    spaces += 1
lines += lines[-2::-1]
for line in lines:   
    print(line)