mark1= int(input("Enter your mark 1: "))
mark2= int(input("Enter your mark 2: "))
mark3= int(input("Enter your mark 3: "))

total_percentage= (mark1+mark2+mark3)/30

if(total_percentage>=40 and  mark1>=33 and  mark2>=33 and  mark3>=33):
    print("You are passed:" , total_percentage)

else:
    print("You are failed")    
