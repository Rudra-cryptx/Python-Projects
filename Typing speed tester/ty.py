from time import *
import random as r
import difflib

def Mistaks(text, usertext):
    matcher = difflib.SequenceMatcher(None, text, usertext)
    accuracy_ratio = matcher.ratio()      # value between 0 and 1
    total_chars = len(text)
    
    errors = round(total_chars * (1 - accuracy_ratio))
    return errors


def speed(time_s,time_e,usertext):
    time_r = round(time_e - time_s , 2)
    ch = len(usertext)
    cps = round(ch/time_r,2)
    wpm = round((ch / 5) / (time_r / 60))

    return cps,wpm

def accuracy(text,usertext):
    error= Mistaks(text,usertext)
    total_char = len(text)
    correcct_char = total_char - error
    acc = (correcct_char/total_char)*100
    return round(acc,3)

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
test = r.choice(strings)
print("_________________________________Typing Speed Tester____________________________")
print ()
print ("   -------Type the following text as fast and accurately as you can-------")
print(test)
print("press enter when you are ready to start...")
input()
time_start = time()
user_text = input("Write text:")
time_end = time()
cps,wpm = speed(time_start, time_end,user_text)
print()
print("Typing speed: " , cps , "Character/sec")
print("Typing speed: " , wpm , "Words/min")
print("No. of ERRORS: " , Mistaks(test, user_text))
print("Accuracy: ", accuracy(test, user_text))


