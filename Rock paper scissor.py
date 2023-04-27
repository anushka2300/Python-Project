import random
def choice():
    print("1.Stone🪨 | 2.Paper🧻 | 3.Scissor✂️")
    ch=int(input("Your choice?\n"))
    if (ch==1 or ch==2 or ch==3):
        return ch
    else:
        phrase=["Whoopsie 🫢...Try again", "Clock is ticking dude⏱...Enter wisely🧙", "Well...even if no one believes in you, I still do😌👼 try again🌟", "Come onnnnn😠😠😡😡....Don't let me down🥹", "Gaadi wala aaya ghar se kachra ni🕺🎶....ohh🙂...you entered wrong🥲...no problem, try again🤧", "Kindly enter correct this time🙂😤🤦"]
        print(phrase[random.randrange(0, len(phrase))])
        return choice()

print("---- 😎STONE, PAPER, SCISSOR😎 ----")
print("Shall we start?😈")
start=input("Enter y/n: ")
score_comp=score_user=0
while (start=="y"):
    ch=choice()
    comp=random.randint(1,3)
    if (ch==1):
        if (comp==1):
            print("Tie!🥴")
        elif (comp==2):
            score_comp+=1
            print("Computer won!😈")
        else:
            score_user+=1
            print("You won!😎")
    elif (ch==2):
        if (comp==2):
            print("Tie!🥴")
        elif (comp==3):
            score_comp+=1
            print("Computer won!😈")
        else:
            score_user+=1
            print("You won!😎")
    else:
        if (comp==3):
            print("Tie!🥴")
        elif (comp==1):
            score_comp+=1
            print("Computer won!😈")
        else:
            score_user+=1
            print("You won!😎")
    print(f'Scores are:\nComputer💻:- {score_comp}\nUser🧑:- {score_user}')
    start=input("Do you want to continue?👼(y/n)\n")
if (start=='n'):
    if (score_comp!=0 and score_user!=0):
        if (score_user>score_comp):
            print(f'You won with {score_user} scores🥳🥳🥳, whereas computer only made upto {score_comp} score')
        else:
            print(f'Computer won with {score_comp} scores🥳🥳🥳, whereas you only made upto {score_user} scores')
    else:
        print("No problem😎, we'll meet soon!😈")