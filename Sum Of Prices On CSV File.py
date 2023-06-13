import csv
def sumprice():
    with open("items.csv","r",newline='') as f:
        sreader=csv.reader(f)
        next(sreader)
        SUM=0
        for i in sreader:
            SUM=SUM+int(i[2])
        print("SUM OF PRICES=",SUM)
sumprice()

