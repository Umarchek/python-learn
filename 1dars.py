"""
a=int(2) #int---integer butun son
b=float(1.2) #float o'ngli kast sonlarni o'z ichiga oladigan tur
c=str('test') #str---string satr yoki matin turi
d=(a)
print(type(d))
"""
#magazin calculator
a=str(input('mahsulot nomi: '))
b=int(input('mahsulot massasi (kg): '))
kartoshka=int(15000)
sabzi=int(2000)
if a == 'kartoshka':
     c=b*kartoshka
     print(c,'so`m')
elif a=='sabzi':
     c=b*sabzi
     print(c,'so`m')