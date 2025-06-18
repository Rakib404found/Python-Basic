class Programmer:
    company= "Microsoft"
    def __init__(self, name, salary, pin):
        self.name= name
        self.salary= salary
        self.pin= pin

p=Programmer("Rakib", 150000, 52165)
print(p.name, p.salary, p.pin)

r=Programmer("Rafsan", 120000, 26549)
print(r.name, r.salary, r.pin)