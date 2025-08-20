num = int(input("enter the number: "))

if num>1:
    for i in range(2,num):
        if num%i ==0:
            print("Not a prime number")
            break
    else:
        print("Is a prime number")
else:
    print("Not a prime number")