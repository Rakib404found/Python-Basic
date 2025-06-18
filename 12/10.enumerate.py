l = [5, 562, 25, 125]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index +=1

#This thing can be simplified by enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")