f= open("poem.txt")
data= f.read()
if("twinkle" in data):
    print("Twinkle this word is here")

else:
    print("Twinkle this word is not here")   

f.close() 