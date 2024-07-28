import time
import threading
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    while True:
        time.sleep(1200)  
        messagebox.showinfo("Alart", "Is time to rest! Please look at around")
        time.sleep(20)
        print("Alarm time set's for 20 min later!")

def start_alarm():
    alarm_thread = threading.Thread(target=set_alarm)
    alarm_thread.start()

root = tk.Tk()
root.title("LookAround")
root.geometry("300x150")

start_button = tk.Button(root, text="Start procces", command=start_alarm)
start_button.pack(pady=20)

root.mainloop()
