import tkinter as tk
import time

def countdown(count):
    label['text'] = count

    if count > 0:
        root.after(1000, countdown, count-1)
    else:
        label['text'] = "Time's up!"

root = tk.Tk()
root.title("专注时钟")
root.geometry("300x200")

label = tk.Label(root, font=("Arial", 80))
label.pack(pady=50)

start_button = tk.Button(root, text="开始", command=lambda: countdown(25*60))
start_button.pack()

root.mainloop()
