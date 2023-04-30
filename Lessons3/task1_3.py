#Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці. 
#На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер квартири 
#та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі. Якщо такої квартира 
#немає в цьому будинку, то необхідно повідомити користувача про це.
#flat=int(input('Flat number=  '))
#porch=(flat - 1) // 36 + 1
#floor=((flat - 1) % 36) // 4 + 1
#if 144 < flat or flat <= 0:
   # print("No such flat in this building")
#else:
    #print("Porch =", porch, "Floor =", floor)

FLOORS = 9
FLATS_IN_FLOOR = 4

flat = int(input('flat number = ')) - 1
entrance = flat // (FLOORS * FLATS_IN_FLOOR) + 1
floor = flat // FLATS_IN_FLOOR - (entrance - 1) * FLOORS + 1
number_in_floor = flat % FLATS_IN_FLOOR + 1

print(flat + 1, entrance, floor, number_in_floor)

#прописати за допомогою фцнкціі
def get_flat_info(flat, FLOORS, FLATS_IN_FLOOR):
    entrance = flat // (FLOORS * FLATS_IN_FLOOR) + 1
    floor = flat // FLATS_IN_FLOOR - (entrance - 1) * FLOORS + 1
    number_in_floor = flat % FLATS_IN_FLOOR + 1

    return entrance, floor, number_in_floor

res = get_flat_info (123, 10 ,50)
print(res)
