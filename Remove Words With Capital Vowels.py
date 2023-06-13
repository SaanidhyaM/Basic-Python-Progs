def convert(lst):
    return (lst[0].split())
f1=open("D:\\Text1.txt")
r1=f1.read()
lst =[r1]
l=[]
print(convert(lst))
for i in convert(lst):
    i=str(i)
    if i[0:1] in ["A","E","I","O","U"]:
        l.append(i)
f2=open("D:\\Text2.txt","w")
for m in range (len(convert(lst))):
    if convert(lst)[m] not in l:
        f2.write(convert(lst)[m])
        f2.write(" ")
f2=open("D:\\Text2.txt","r")
r2=f2.read()
print(r2)
        


        


