def convert(lst):
    return (lst[0].split())
f1=open("D:\\LINE.txt")
r1=f1.read()
lst = [r1]
m=0
for i in convert(lst):
    i=str(i)
    if i[0:1] in ["A","a"]:
        m+=1
print("No. of words starting from A or a: ",m)

