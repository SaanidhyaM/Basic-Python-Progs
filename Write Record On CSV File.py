import csv
def write():
    with open("items.csv","w",newline='') as f:
        swriter=csv.writer(f)
        swriter.writerow(["ITEMNO","NAME","PRICE"])
        rec=[]
        while(True):
            INO=int(input("ENTER THE ITEM NO: "))
            NAME=input("ENTER THE ITEM NAME: ")
            PRICE=int(input("ENTER THE PRICE: "))
            LIST=[INO,NAME,PRICE]
            rec.append(LIST)
            CH=input("DO YOU WANT TO CONTINUE?: ")
            if CH=="n":
                break
        swriter.writerows(rec)
write()
    
