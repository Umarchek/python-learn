"""
a=['olma','banan','nok'] #Array
print(a[0])

#CheckDays
oy=int(input('oyning tartib raqamini kiriting: '))
if oy==2:
	kun=28
elif oy in [1,3,5,7,8,10,12]:
	kun=31
else :
	kun=30
print(oy,'oy ',kun,'kundan iborat')

#while test
k=1
while k<=100:
	print(k)
	k+=1 #kga 
	#2ni qo'shish #faqat 10gacha kirgizadi chunki 10dan keyn 10dan katta bo'ladi
"""
#for
for i in 'salom dunyo':
	print(i*2,end=' ')

	