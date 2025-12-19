# ⌨️ Typing Speed Tester — Python

A command-line **Typing Speed Tester** built in Python.  
It measures:
- ⏱️ Time taken
- ⚡ Characters Per Second (CPS)
- 🚀 Words Per Minute (WPM)
- ❌ Number of Errors
- 🎯 Accuracy Percentage

Unlike simple typing testers, this project uses Python’s `difflib.SequenceMatcher`
to calculate **realistic typing mistakes and accuracy** instead of strict
character-by-character comparison.

---

## 📸 How It Works
1️⃣ A random sentence is displayed  
2️⃣ Press **Enter** to start  
3️⃣ Type the sentence  
4️⃣ Program calculates:
- Time taken
- CPS
- WPM
- Mistakes
- Accuracy %

---

## 🧠 Features
✔️ Random sentence generator  
✔️ Smart mistake detection using `difflib`  
✔️ Accurate WPM calculation (industry formula)  
✔️ Character per second speed  
✔️ Accuracy percentage  
✔️ Simple and beginner friendly  
✔️ No external installation needed

---

## 🛠️ Tech Stack
- **Language:** Python
- **Modules Used:**  
  - `time`
  - `random`
  - `difflib`

All modules are built-in — no extra install required.

---

## ▶️ Run the Project
1️⃣ Make sure Python is installed  
2️⃣ Save the file as:
3️⃣ Run in terminal / command prompt:


---

## 📌 Output Example
_____Typing Speed Tester

-------Type the following text as fast and accurately as you can-------
Practice typing properly instead of just quickly, and speed will automatically follow.
Press enter when you are ready to start...

Write text: Practice typing properly instead of just quickly, and speed will automatically follow.

Typing speed: 2.85 Character/sec
Typing speed: 34 Words/min
No. of ERRORS: 3
Accuracy: 96.72 %

Errors are calculated using smart similarity matching:
`difflib.SequenceMatcher`

---

## 🚀 Future Enhancements
🔹 GUI Version (Tkinter)  
🔹 Highlight mistakes  
🔹 Countdown timer  
🔹 Difficulty levels  
🔹 Real-time typing stats

---

## 🙌 Author
Developed by **Rudra**  
Feel free to connect on LinkedIn 🙂

---

## ⭐ Contribution
Pull requests are welcome!  
If you liked this project, don’t forget to ⭐ star the repo.

---
