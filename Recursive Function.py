def disp(x):
    print(x)
    if x>0:
        y=disp(x-1)
    else:
        y=0
    return y
num=int(input("enter a value: "))
disp(num)
