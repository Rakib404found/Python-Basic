f= open("file.txt", "r") #  open the file in read mode
data=f.read() # read its content

print(data)
f.close() # close the file