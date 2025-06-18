class Employee:
    language = "py"
    salary = 120000

    def __init__(self, name, salary, language):  # ✅ ঠিকঠাক constructor
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


rakib = Employee("Rakib", 1300000, "JavaScript") 
print(rakib.name, rakib.salary, rakib.language)

rohan = Employee("Rohan", 100000, "Python")
print(rohan.name, rohan.salary, rohan.language)
