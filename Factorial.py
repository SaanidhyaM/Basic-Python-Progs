def disp(x):
    i=x
    if x-1 >0:
        i=x*disp(x-1)
    return i
num=int(input("enter a value: "))
print("factorial=",disp(num))

