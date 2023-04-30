#Task 6
#Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
#Наприклад: XXII -> 22
#Докладніше: https://en.wikipedia.org/wiki/Roman_numerals
def func(**kwargs):
    
    print(kwargs) 
print(func(i=1, ii=2))   
rome  = {
    I: "one",
    II: "February",
    III: "March",
    IV: "April",
    V: "May",
    VI: "June",
    VII: "July",
    VIII: "August",
    IX: "September",
    X: "October",
    
}
month = int(input('enter the month='))
print(months.get(month, 'Error'))
