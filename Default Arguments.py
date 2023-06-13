def fun(SId,SName, Atten, Marks=0):
    print("Student with ID-",SId,"and Name-",SName,"has scored-", Marks,"Marks. He was",Atten)
SId=int(input("Enter Student ID: "))
SName=input("Enter Student Name: ")
Atten=input("Enter if Absent or Present: ")
if Atten=="Present":
    Marks=int(input("Enter marks: "))
    fun(SId, SName, Atten, Marks)
else:
    fun(SId, SName, Atten)
