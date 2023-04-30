days = {
    1: 'пн', 
    2: 'вт', 
    3: 'ср', 
    4: 'чт', 
    5: 'пт', 
    6: 'сб', 
    7: 'нд'
}
#day = int(input('day='))
#if 1 <= day <= 7:
#    print(days[day])
#else:
#    print('Error')

#day = int(input('day='))
#if day in days:
#    print(days[day])
#else:
#    print('Error')

day = int(input('day='))
print(days.get(day, 'Error'))