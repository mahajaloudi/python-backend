
num = int(input("Enter number:"))
flage = True
if num<= 1 :
    print(" not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            flage = False
            break
if flage:
    print("prime")
else:
    print("not prime")