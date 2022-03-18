a=9 #int - intager butun son
b=6 #float 10lik kasr son
c=[4,5,6,7]
#print(a//b)

"""
if a<b:
	print('a b dan kichik')
	
elif a>b:
	print('a b dan katta')

if a==b:
	print(a ,"va",b,'biriga teng')

elif a!=b:
	print('a va b biriga teng emas ')
if a in c:
	print('a c da mavjud')
else:
	print('a c da mavjud mas')
"""
#mini calculator
"""
a=int(input('birinchi sonni kiriting: '))
b=int(input('ikkinchi sonni kiriting: '))
c=str(input('amalni kiriting: '))
if c=='+':
	print(a+b)
if c=='/':
	print(a/b)
"""	

#Homework start
a=int(input('Iltimos birinchi sonni kiriting: '))
b=int(input('Iltimos ikkinchi sonni kiriting: '))
textAmal='Iltimos amalni kiriting: '
error='kechirasiz bunaqa amal xali bizda mavjud emas :)))'
if b:
	Amallar=str(input(textAmal))
if Amallar=="+":
	print('agar',a,'ni',b,'ga qoshsak',a+b,'javobi chiqadi :)')
elif Amallar=="-":
	print('agar',a,'dan',b,'ni ayrsak',a-b,'javobi chiqadi :)')
elif Amallar=="*":
	print('agar',a,'ni',b,"ga ko'paytirsak",a*b,'javobi chiqadi :)')
elif Amallar=="/":
	print('agar',a,'ni',b,"ga bo'lsak",a/b,'javobi chiqadi :)')
else:
	print(error)