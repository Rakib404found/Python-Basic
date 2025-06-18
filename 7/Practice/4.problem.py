n= int(input("Enter your number: "))

for i in range(2, 20):
    if(n%i  == 0):
        print("Number is not prime")
        break

else:
    print("Number is prime")