from random import randint

n = randint(1,100)

a = -1

guess = 0

while(a!=n):
    guess = guess + 1
    a = int (input("Enter the number: "))

    if(a>n):
        print("Enter lower number.")
    else:
        print ("Enter higher number.")

print (f"The number has being guessed by you in the {guess} no. of try.")
