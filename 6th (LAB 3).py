a=int(input("enter a number "))
b=int(input("enter a number "))
c=int(input("enter a number "))
if(a>b):
    a=a+b
    b=a-b
    a=a-b
if(a>c):
    a=a+c
    c=a-c
    a=a-c
if(b>c):
    b=b+c
    c=b-c
    b=b-c
print(a,"<",b,"<",c)
