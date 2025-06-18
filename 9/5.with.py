f = open("file.txt")
print(f.read())
f.close()

# This same can be written using with statement like this

with open("file.txt") as f:
    print(f.read())

# You do not have to close this file 