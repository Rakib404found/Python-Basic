with open("old.txt", "r") as f:
    content= f.read()

with open("renamed by pyhon.txt", "w") as f:
    f.write(content)    