import os
import pickle 
stu={} 
stufile1=open("temp.dat",'ab')
stufile=open("Stu.dat",'rb')
r=int(input("Enter the roll no. you want to update: "))
try: 
    while True: 
        s=pickle.load(stufile)
        if r in s:
            s[1]=input("Enter New name: ")
        pickle.dump(s,stufile1)
except EOFError:
    stufile1.close()
    stufile.close()
os.remove("Stu.dat")
os.rename("temp.dat","Stu.dat")
stufile=open("Stu.dat",'rb')
try: 
    while True: 
        s=pickle.load(stufile)
        print(s)
except EOFError:
    stufile.close()
