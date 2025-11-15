from random import randint as r

def roll_dice():
    
    roll = (r(1,6), r(1,6))  
    return roll 

def main():
    while True:
        print("Enter 'Y' to roll the dice or 'N' to exit:")
        user_input = input().strip().upper() 
        if user_input == 'Y':
            
            print(f"Your dice rolled the dice: {roll_dice()} ")
        elif user_input == 'N':
            print("Exiting the dice roll. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Y' or'N'.")    

if __name__ == "__main__":
    main()

