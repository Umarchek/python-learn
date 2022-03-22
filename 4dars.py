# a="""Salom dunyo 
# bu ko'p qatorli 
# satr"""
# print(a)

# a='salom'
# #  01234
# print(a[1:5]) #1chi elemdan 4chi elemgacha

#Strip - bo'sh joylarni ob tashlaydi
# a='  salomlar  '
# print(a.strip())

#Lower - satrdagi barcha harflarni kichkina yozuvda
# a='Markaziy osiyo'
# print(a.lower())

#Upper - satrdagi barcha harflarni katta yozuvda
# a='markaziy osiyo'
# print(a.upper())

#Replace - o'zgartirib beradi
# b='Sog` tanda sog`lom aql'
# print(b.replace('aql','birnarsa'))

#Split satrni ajratib chiqadi
# a='Python bilan ishlash Juda Ajoyib'
# print(a.split(" "))

# a='Ey san pubg uynashni bilmesan san bot san'
# x="bot" in a
# if x==True:
# 	print('Iltimos xaqoratli so`zlar ishlatmang')

#format valueni qo'yib beradi.
# yosh=input('yoshingizni kiriting: ')
# matn='Sizning yoshingiz {}da '
# print(matn.format(yosh))

#Set qushib beraadi

toq={1,3,5,7,9}
juft=set((2,4,6,8))
print(toq,juft)