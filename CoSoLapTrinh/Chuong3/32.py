a=int(input('M1= '))
b=int(input('M2= '))
c=int(input('M3= '))
d=int(input('S= '))
if d<=100:
    print('Phai tra= ',(d*a))
elif 101<=d<=150:
    print('Phai tra= ',(100*a+(d-100)*b))
else:
    print('Phai tr= ',(100*a+50*b+(d-150)*30))  