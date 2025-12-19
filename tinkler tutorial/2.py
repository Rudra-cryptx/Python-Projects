import tkinter as tk
root = tk.Tk()
root.title("This is to add button")
def button():
    lable.config(text="You Clicked the button.")

root.geometry("400x400")
lable = tk.Label(root , text="Click the button" , font=("Arial", 20))
lable.pack()    
btn = tk.Button(root , text="Click me", font=("Arial", 16) , command=button)
btn.pack()
root.mainloop()