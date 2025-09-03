def Multiplication(a,b,c):
    multi = a * b * c
    return multi

def Addition(a,b,c):
    add = a + b + c
    print(add)
print(Addition(34,52,45))


def Sum_Number(*n):
    total = 0
    for i in n:
        total += i
    return total
print(Sum_Number(5,5,6,4))
