#Task 3
#Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, 
#скільки разів яка літера зустрічається в цьому рядку.
#Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
#res = {}
#text = input('text=')
#for item in text:
#    if item not in res:
#        res[item] = text.count(item)
#print(res)


text = input('text=').lower()
result = {}
for item in text:
    if item.isalpha() and item not in result:
        result[item] = text.count(item)
res = '\n'.join(map(lambda item: f'{item[0]} - {item[1]}', result.items()))
print(res)
