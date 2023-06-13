def show(f1,f2):
    f1=open("D:\\1.txt")
    r1=f1.read()
    l1=[]
    l1=r1.split("  ")
    f2=open("D:\\2.txt",'w')
    for i in l1:
        f2.write(i)
        f2.write(" ")
    f1=open("D:\\1.txt","r")
    f2=open("D:\\2.txt","r")
    print("Original File=",f1.read())
    print("New File=",f2.read())
n=0
m=0
show(n,m)
