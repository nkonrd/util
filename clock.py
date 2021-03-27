import sys, time
import tkinter as tk

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)

root = tk.Tk()

clock = tk.Label(root, font = ("times", 100, "bold"), bg="white")
clock.grid(row=1, column=0)

date_string = time.strftime("%A, %b %d")
date = tk.Label(root, font = ("times", 16, "bold"), bg="white", text=date_string)
date.grid(row=0, column=0)
    
tick()
root.configure(bg="white")
root.title("time") 
root.mainloop()
