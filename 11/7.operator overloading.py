class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = number(5)
m = number (10)

print(n+m)