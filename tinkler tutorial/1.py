import tkinter as tk
root = tk.Tk()
root.title("My first app")
root.geometry("400x400")
lable = tk.Label(root,text="Hello Rudra" , font=("Arial",20))
lable.pack()
root.mainloop()