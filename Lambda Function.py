x=lambda a,b,c:a*b*c
print(x(4,5,6))

def disp(n):
    return lambda a:a**n
x=disp(3)
print(x(5))
