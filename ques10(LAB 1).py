num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
op=input("enter any operator: ")
if(op=='+'):
    print("sum of two number is",num1+num2)
elif(op=='-'):
     print("difference of two number is",num1-num2)
elif(op=='*'):
     print("product of two number is",num1-num2)
elif(op=='/'):
     print("division of two number is",num1-num2)
else:
    print("invalid operator")
