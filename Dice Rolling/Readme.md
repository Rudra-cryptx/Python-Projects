# 🎲 Dice Roller Program (Python)

This is a simple Python program that simulates rolling two dice.  
The user can press **Y** to roll the dice or **N** to exit the program.

---

## 🚀 Features
- Rolls two dice using Python's `randint()`
- Random results between **1 to 6**
- User-friendly interactive input
- Runs in a loop until the user chooses to exit
- Simple and beginner-friendly structure

---

## 📌 How It Works
1. The program uses `randint(1, 6)` to generate two random numbers.
2. When the user enters **Y**, a new dice roll is displayed.
3. When the user enters **N**, the program exits.
4. Invalid inputs show an error message.

---

## 📄 Code

```python
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
            print("Invalid input. Please enter 'Y' or 'N'.")    

if __name__ == "__main__":
    main()

🧪 Example Output:
Enter 'Y' to roll the dice or 'N' to exit:
Y
Your dice rolled the dice: (4, 2)

Enter 'Y' to roll the dice or 'N' to exit:
N
Exiting the dice roll. Goodbye!

📦 Requirements

Python 3.x

No external libraries required