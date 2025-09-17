from random import choice
def play():
    you = 0
    my_self = 0
    for rand_no in range(1,6):
        user = input("Enter the choice stone/paper/scissor:  ").lower()
        options = ["stone" , "paper" , "scissor"]
        result = choice(options)
        print (f"The computer choice is {result}")

        if (user == result):
            print("It's a tie.")
            you = you + 1
            my_self = my_self + 1

        elif(user =="paper" and result =="stone") or (user == "stone" and result=="scissor") or (user == "scissor" and result == "parer"):
            print("you win.")
            my_self =my_self + 1
        else:
            print ("you loss this round.")
            you = you + 1

    if(you>my_self):
        print (f"The overall winner is Computer with {you} pointe")
    elif(you==my_self):
        print("The match is tie.")
    else:
        print (f"You are the overall winner with the  {my_self} points")
    
play()