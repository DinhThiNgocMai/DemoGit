import math
a=float(input('x= '))
b=float(input('y= '))
ch=input('Phep toan:')
if ch=='+':
    print(str(a)+ch+str(b)+'=', round(a+b, 1),sep="")
elif ch=='-':
    print(str(a)-ch-str(b)+'=', round(a-b, 1),sep="")
elif ch=='*':
    print(str(a)*ch*str(b)+'=', round(a*b, 1),sep="")
elif ch=='/':
    if b==0:
        print('Khong hop le')
    else:
        print(str(a)/ch/str(b)+'=', round(a/b, 1),sep="")
else:
    print('Khong hop le')
   
    