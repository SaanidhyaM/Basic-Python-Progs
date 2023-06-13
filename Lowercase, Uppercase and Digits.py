def show():
    f1=open("D:\\Book.txt")
    r1=f1.read()
    d={"Upper":0,"Lower":0,"Digits":0}
    for i in r1:
        if i.isupper():
            d["Upper"]+=1
        elif i.islower():
            d["Lower"]+=1
        elif i.isnumeric():
            d["Digits"]+=1
    print("FILE=",r1)
    print(d)
show()
