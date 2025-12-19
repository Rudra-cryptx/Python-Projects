import tkinter as tk
from time import *
def start():
    global start
    start = time()
    lable.config(text="Time started type something")
def stop():
    end = time()
    total_time = round(end - start , 2)
    lable.config(text=f"Your thime you took to write is: {total_time}")

root = tk.Tk()        
root.geometry("500x500")
root.title("TEST")

lable = tk.Label(root , text="Enter start " , font=("Arile" , 22))
lable.pack(pady=20)

st_btn = tk.Button(root , text="Start" , font=("Arile" ,18) , command=start)
st_btn.pack()

so_btn =tk.Button(root , text="Start" , font=("Arile" ,18) , command=stop)
so_btn.pack()




root.mainloop()