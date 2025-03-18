num=int(input("enter  a number"))
if(num<1 or num==1):
    print("it is not a prime number")
if(num>1):
    for i in range(2,num-1):
        if(num%i !=0):
            flag=True 
            break
    if flag:
        print("It is a prime number")
    else:
        print("It is not a prime number ")
