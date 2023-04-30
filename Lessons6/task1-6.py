#Task 1
#Використовуючи словник, напишіть програму, яка виведе на екран назву місяця за номером.
months  = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
month = int(input('enter the month='))
print(months.get(month, 'Error'))
