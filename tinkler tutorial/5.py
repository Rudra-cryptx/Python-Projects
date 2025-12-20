import tkinter as tk 
import random as r

strings = [
    "The quick brown fox jumps over the lazy dog and keeps running into the distant forest.",
    "Programming requires patience, practice, and the ability to think logically under pressure.",
    "Typing speed improves when you focus on accuracy first instead of rushing through the text.",
    "Technology is evolving rapidly, and learning new skills has become more important than ever.",
    "Consistency is the key to mastering any skill, whether it is coding, writing, or speaking.",
    "A good typing speed tester helps users track their progress and improve their accuracy over time.",
    "Discipline and dedication separate dreamers from achievers in almost every field of life.",
    "When you learn to stay calm and focused, even the hardest challenges start to feel manageable.",
    "Many people underestimate how powerful small daily improvements can become over a long period.",
    "Reading regularly helps improve vocabulary, comprehension, and overall communication skills.",
    "Errors are a natural part of learning, and each mistake teaches you something valuable.",
    "Practice typing properly instead of just quickly, and speed will automatically follow."
]

def btnn():
    global test_text
    test_text = r.choice(strings)
    text_lable.config(text=test_text)
    entry.delete(0,tk.END)
    entry.focus()

root = tk.Tk()
root.title("Test 5")
root.geometry("500x500")
root.config(bg="black")

title  = tk.Label(root , text="Typing speed tester.." , font=("Arile" , 22 , "bold") , fg="blue" ,bg="black" )
title.pack(pady=20)

text_lable = tk.Label(root , text="Click the start button to start typing speed." , wraplength=450 , bg="black" , fg="white" , font=("Arile " , 18))
text_lable.pack(pady=10)

entry = tk.Entry(root , font=("Arile" , 20)  , bg="black" , fg="white")
entry.pack(pady=10)

start_btn = tk.Button(root, text="Start" , font=("Arile" , 16) , bg="black" , fg="yellow" , command=btnn)
start_btn.pack(pady=10)
root.mainloop()