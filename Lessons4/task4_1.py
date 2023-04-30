number = input()
number = list(map(int, number))
mid = len(number) // 2

if sum(number[:mid]) == sum(number[mid:]):
    print('Lucky')
else:
    print('Not Lucky')

#або res = 'Lucky' if sum(number[:mid]) == sum(number[mid:]) else 'Not Lucky'
# print(res)     