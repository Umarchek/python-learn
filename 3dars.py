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
#for
for i in 'salom dunyo':
	print(i*2,end=' ')
#len (read)
a=['mening','hp','laptopim','bor']
for i in range(len(a)):
	print(i,a[i])

#break
for i in 'salom dunyo':
	if i=="o":
		#break
		continue
	print(i*1,end=" ")

#def func
def func(n):
	a,b=0,1
	while b<n:
		print(b)
		a,b=b,a+b
func(2000)

#def raqamlar
def raqamlar(n):
	sum=0
	while n!=0:
		sum+=n%10
		n=n//10
	return sum
s=int(input('istagan sonni kiriting: '))
print('siz kiritgan sonning raqamlar yig`indisi',raqamlar(s),'ga teng')
"""
#homework
import msvcrt, sys
kitoblar=str(input('Kitobni kiriting: '))

# for i in kitoblar:
# 	if kitoblar !='stop':
# 		print(kitoblar)
# 	elif kitoblar == "stop":
# 		print(i)
# 		sys.exit()

while kitoblar!='stop':
	kitoblar=str(input('Kitobni kiriting: ')) 
if kitoblar=='stop':
	print(kitoblar)