#Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої. 
#Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує 
#такий трикутник.
#A = int (input('A='))
#B = int (input('B='))
#C = int (input('C='))
#if (A + B > C) and (B + C > A) and (A + C > B):
 #   print ('Трикутник існує')
#else:
 #   print ('Трикутник не існує')

a, b, c = int(input('a=')), int(input('b=')), int(input('c='))

if a + b > c and b + c > a and a + c > b:
    print('Ok')
else:
    print('Error')