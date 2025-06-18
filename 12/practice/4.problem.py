try:
    a= int(input("Enter your 1 number:"))
    b= int(input("Enter your 2 number:"))
    print(a/b)

except ZeroDivisionError as e:
    print("Infinite")