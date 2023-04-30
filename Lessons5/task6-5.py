#Task 6
#Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися з однієї літери). 
#Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту. Напишіть програму, яка визначить
#найкоротше слово з написаних Вовочкою. Наприклад:
#aaaaaaa - Вовочка писав слово - "a"
#ititititit - Вовочка писав слово - "it"
#catcatcatcat - Вовочка писав слово - "cat"

text = input('text=')

mid = len(text) // 2 + 1 if len(text) % 2 else len(text) // 2

for i in range(mid):
    tmp = text[:i + 1]
    if len(tmp) * text.count(tmp) == len(text):
        print(tmp)
        break
else:
    print('Error')
