# Написати програму, яка буде повертати для заданого року кількість днів. 
#Рік є високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400

#year = int(input('year='))
#if year % 400==0 or year % 4==0 and year % 100!=0:
 #   print('Високосний рік')    
#else:
 #   print('Не високосний рік')

year = int(input('year='))
days = 366 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 365
print(days) 
   