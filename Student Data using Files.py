f1=open("D:\\l.txt",'w')
for n in range(0,5):
    rollno.=input("Enter Roll No.: ")
    name=input("Enter Name: ")
    marks=input("Enter Marks: ")
    rec=rollno+","+name+','+marks+'\n'
    f1.write(rec)
f1.close()
f1.open("D:\\l.txt",'r')
print(f1.read())
