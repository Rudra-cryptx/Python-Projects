import tkinter as tk

root = tk.Tk()
root.geometry("500x500")

lable = tk.Label(root, text=("This is 3rd program.") , font=("Arial", 22))
lable.pack()

enter = tk.Entry(root , font=("Arial" , 18) , width=40)
enter.pack()
root.mainloop()