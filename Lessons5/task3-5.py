#Task 3
#Напишіть скрипт, який обчислює суму всіх кодів символів рядка.
'''
text = input('text')
a = 0
for i in text:
    a += ord(i)   
print(a)
word=str(input())
b=[ord(a) for a in word]
print(sum(b))   
'''

name = input('name=')
s = [ord(item) for item in name]
print(sum(s)) 

#name = input('name=')
#s = 0
#for item in name:
#    s += ord(item)
#print(s)
