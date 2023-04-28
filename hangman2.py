import random
def word():
    l=['player','brave','proctor','stand','great','manager']
    x=random.choice(l)
    return x
def hang(j):
    hang1=['''
   
   
   
   
   
           --------''','''
   
   
   
   
   
           --------
           --------''','''
              |
              |
              |
              |
           --------
           --------''','''
      +-------+
              |
              |
              |
              |
           -------
           -------''','''
      +-------+
      O       |
              |
              |
              |
           -------
           -------''','''
      +-------+
      O       |
      |       |
              |
              |
           -------
           -------''','''
      +-------+
      O       |
    / |       |
              |
              |
           -------
           -------''','''
      +-------+
      O       |
    / | \     |
              |
              |
           -------
           -------''','''
      +-------+
      O       |
    / | \     |
     |        |
              |
           -------
           -------''','''
      +-------+
      O       |
    / | \     |
     | |      |
              |
           -------
           -------''']
    print(hang1[j])

    
w=word()
print("RULES: YOU WILL BE GIVEN 10 TURNS TO CHOOSE THE LETTER.EACH WRONG TURN WILL DRIVE THE MAN TOWARDS DEATH.😢")
n=input("enter your name:")
find="_"*len(w)
print(find)
j,rg,wg=0,0,0
flag=0
missed=""
for i in range(10):
    print("Guess the letter:")
    alpha=input()
    if(alpha in w):
       index= w.index(alpha)
       print("WELL DONE!!")
       find=find[:index]+alpha+find[index+1:]
       print(find)
       rg=rg+1
       if("_" not in find):
           print("HURRRAAYYY!!, You Won.🥳🥳🥳")
           flag=1
           break
    else:
        print("ooops,You missed!!☹️")
        missed=missed+alpha+" "
        print("missed letters:",missed)
        hang(j)
        wg=wg+1
        j=j+1
        if(j==9):
            print("HE DIED!😓,YOU LOST!!")
    print(9-i,"Guesses left..")
print(n,"made",wg," wrong guesses and",rg,"correct guess,and the word is",w)
    
