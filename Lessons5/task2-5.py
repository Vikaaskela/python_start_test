#Task 2
#Користувач вводить з клавіатури ім'я людини. 
#Написати програму для перевірки введеного ім'я на валідність 
#(мається на увазі, що, наприклад, в імені людини не може бути цифр, воно повинно 
#починатися з великої літери, за якою повинні йти маленькі).

name = input('name=')

if name.istitle():
    name = name.split()
    for word in name:
        if not word.isalpha():
            print('Error')
            break
    else:
        print('It is name')
else:
    print('Error')