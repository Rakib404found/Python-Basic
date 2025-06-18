def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 36564, 55, 54974, 65, 54854854]

f= list(filter(divisible5, a))
print(f)