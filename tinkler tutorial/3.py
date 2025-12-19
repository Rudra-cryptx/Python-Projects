import tkinter as tk
root = tk.Tk()
root.geometry("500x900")
def button():
    user_text = lable.get()
    result.config(text=f"your Typed text {user_text}")
root.title("This is try")

lable = tk.Entry(root,   font=("Arile" , 20))
lable.pack(pady=10)

btn = tk.Button(root , text="Submit" , font=("Arile" , 18) , command=button) 
btn.pack()

result = tk.Label(root, text="" , font=("Arile", 24))
result.pack(pady=20)

root.mainloop()