print("this is a number guessing game")
print("choose a number in your mind computer will find it.")
guess = int(input("press 1 if less than 5 or 2 for greater than 5"))
if(guess==1):
    guess1 = int(input("press 1 if greater than 3 or 2 for less than 3"))
    if(guess1==1):
            guess2 = int(input("press 1 if greater than 4 or 2 for less than 4 AND  3 if equal to 4:"))
            if(guess2==1):
                print("your number is 3")
            elif(guess2==2):
                print("your number is 5")
            elif(guess2==3):
                print("your number is 4")
    elif(guess1==2):
            guess2 = int(input("press 1 if greater than 2 or 2 for less than 2 AND  3 if equal to 2:"))
            if(guess2==1):
                print("your number is 1")
            elif(guess2==2):
                print("your number is 3")
            elif(guess2==3):
                print("your number is 2")
elif(guess==2):
    guess1 = int(input("press 1 if greater than 7 or 2 for less than 7"))
    if(guess1==1):
            guess2 = int(input("press 1 if greater than 8 or 2 for less than 8 AND  3 if equal to 8: "))
            if(guess2==1):
                print("your number is 10")
            elif(guess2==2):
                print("your number is 7")
            elif(guess2==3):
                print("your number is 8")
    elif(guess1==2):
            guess2 = int(input("press 1 if greater than 6 or 2 for less than 6 AND  3 if equal to 6: "))
            if(guess2==1):
                print("your number is 7")
            elif(guess2==2):
                print("your number is 5")
            elif(guess2==3):
                print("your number is 6")
