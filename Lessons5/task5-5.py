#Task 5
#Вводиться з клавіатури користувачем текст. 
#Знайти в ньому найдовше слово та вивести його на екран.

#text = input('text=')
#x = sorted(text.split(), key=len)
#print(x[-1])    

text = input().split()
max_word = text[0]
for item in text:
    if len(item) > len(max_word):
        max_word = item
print(max_word)

#print(max(text, key=len))