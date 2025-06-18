class Employee:
    language= "py"  # This is a class attribute
    salary = 120000

Rakib=  Employee()
Rakib.name= "Rakib" # This is an instance attribute   
print(Rakib.name, Rakib.language, Rakib.salary)

Rafsan = Employee()
Rafsan.name= "Rafsan"
print(Rafsan.name, Rafsan.language,Rafsan.salary)

#Here name is instance attribute and salary, language are class attributes as they diectly belong to class