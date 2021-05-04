def Game():
    import random
    randnumber = random.randint(1,100)
    #print(randnumber)
    userguess = None
    guess = 0
    while(userguess!=randnumber):
        userguess = int(input("Guess The Number :\n"))
        guess+=1
        if userguess==randnumber:
            print("You Guessed It Right")
        else:
            if userguess<randnumber:
               print("You guessed it wrong ! Enter A Larger Number")
            else:
               print("You guessed it wrong ! Enter A Smaller Number")
    print(f"You Guessed the number in {guess} guesses")
    with open('highscore.txt') as f:
        highscore = int(f.read())
        if highscore>guess:
             print(" Congratulations ! You Have Broken A High Score")
             with open('highscore.txt','w') as f:
                 f.write(str(guess))
        else:
            print(f"the High score is : {highscore}")
while True:
    Game()
    userchoice = input("Do You Want To Play Again yes/NO \n")
    if userchoice=="yes": 
        continue
    else:
        print("Thank You For Playing")
        break