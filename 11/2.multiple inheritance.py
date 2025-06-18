class Employee:
    company = "ITC"
    name= "Default Name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.company}")

class Coder:
    language= "Python"
    def printLanguage(self):
        print(f"Here is yours language: {self.language}")
              

class Programmer(Employee, Coder):
    company= "ITC Infotech"
    def showlanguage(self):
        print(f"The name of the company is: {self.company}. He is good at {self.language} language")



a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showlanguage()