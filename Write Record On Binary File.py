import pickle
stu={}
stufile=open("Stu.dat",'ab')
ans='y'
while ans=='y':
    r=int(input("Enter roll no.: "))
    n=input("Enter name: ")
    pickle.dump([r,n],stufile)
    ans=input("Do you want to input more records?[y/n]: ")
stufile.close()
stufile=open("Stu.dat",'rb')
try:
    while True:
        s=pickle.load(stufile)
        print(s)
except EOFError:
    stufile.close()
