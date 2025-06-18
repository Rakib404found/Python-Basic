a="Make a lot of mone"
b="buy now"
c="subscribe this"
d="click this"

message=input("Enter your comments: ")

if(a in message or b in message or c in message or d in message):
    print("Get lost. This is spam comment")

else:
    print("This is not spam comment")