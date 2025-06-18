try:
    a = int(input("Enter your number: "))
    print(a)

except ValueError as v:
    print("Heyyyyyyy")
    print(v)

except Exception as e:
    print(e)

print("Thank you")