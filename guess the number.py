import random
print("***WELCOME TO THE GUESSING GAME***")
print('''RULES: *FOR EACH CORRECT GUESS YOU WILL BE AWARDED 10 POINTS AND WRONG GUESS WILL BE AWARDED WITH -1 POINTS
     *USER NEED TO ENTER THE NUMBER BETWEEN 1 AND 20''')
a=random.randrange(1,20)
n=input("Enetr your name:-")
s=0
while True:
    print("Test your luck and enter the number:")
    x=int(input())
    if(x==a):
        print("HURRAAY!!",n,"your lucky number is",a)
        s=s+10
        print("Do you want to play more? Y/N")
        c=input() 
        a=random.randrange(1,20)
        if(c=='N'):
            break 
    else:
        s=s-1
        print("oops!!Wrong answer")
print("Final Score is:",s)
               
    
