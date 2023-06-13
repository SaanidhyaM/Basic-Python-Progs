zimport random
while (True):
    i=random.randint(1,6)
    r=input("Enter to Play: ")
    print("You Rolled",i)
    ch=input("Want to play again?:  ")
    if ch=='n':
        break
