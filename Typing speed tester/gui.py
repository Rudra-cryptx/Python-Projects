import tkinter as tk 
import random as r 
from time import *
import difflib

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

def Mistaks(text, usertext):
    matcher = difflib.SequenceMatcher(None, text, usertext)
    accuracy_ratio = matcher.ratio()
    total_chars = len(text)
    errors = round(total_chars * (1 - accuracy_ratio))
    return errors

def accuracy(text,usertext):
    error = Mistaks(text,usertext)
    total_char = len(text)
    correct_char = total_char - error
    acc = (correct_char / total_char) * 100
    return round(acc, 2)

def check_result():
    end_time = time()
    total_time = round(end_time - start_t, 2)

    if total_time == 0:
        total_time = 0.01

    user_text = entry.get()

    chars = len(user_text)

    cps = round(chars / total_time, 2)
    wpm = round((chars / 5) / (total_time / 60))

    err = Mistaks(test, user_text)
    acc = accuracy(test, user_text)

    fin_result.config(
        text=f"Time: {total_time} sec\nCPS: {cps}\nWPM: {wpm}\nErrors: {err}\nAccuracy: {acc}%"
    )

def start():
    global test , start_t
    test = r.choice(strings)
    text_lable.config(text=test)
    entry.delete(0,tk.END)
    entry.focus()
    start_t = time()



root = tk.Tk()
root.geometry("600x550")
root.title("Final")
root.config(bg="black")

titel = tk.Label(root, text="_____Typing speed test_____" , bg="black" , fg="blue" , font=("Arile", 24, "bold"))
titel.pack(pady=10)

text_lable = tk.Label(root , text="Click the start button to test your speed..." , bg="black" , fg="white" , font=("Arile", 20) , wraplength=540)
text_lable.pack(pady=10)

entry = tk.Entry(root , font=("Arile " , 18) )
entry.pack(pady=10)

st_btn = tk.Button(root , text="START" , font=("Arile" , 18) , command=start)
st_btn.pack(pady=10)

en_btn = tk.Button(root , text="RESULT" , font=("Arile" , 18) , command=check_result)
en_btn.pack(pady=10)

fin_result = tk.Label(root , font=("Arile" , 20 , "bold") , wraplength=540 , bg="black", fg="white")
fin_result.pack(pady=10)
root.mainloop()