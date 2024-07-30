import time
import threading
import tkinter as tk
from tkinter import messagebox

def set_alarm(stop_event):
    while not stop_event.is_set():
        time.sleep(1200)  
        messagebox.showinfo("Alert", "It's time to rest! Please look around")
        time.sleep(20)
        print("Alarm time set for 20 minutes later!")

def start_alarm():
    global alarm_thread, stop_event
    stop_event = threading.Event()
    alarm_thread = threading.Thread(target=set_alarm, args=(stop_event,))
    alarm_thread.start()
 
def stop_alarm():
    global alarm_thread, stop_event
    if alarm_thread is not None:
        stop_event.set()
        alarm_thread.join()
        alarm_thread = None
        stop_event = None

root = tk.Tk()
root.title("LookAround")
root.geometry("300x150")

start_button = tk.Button(root, text="Start process", command=start_alarm)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_alarm)
stop_button.pack(pady=30)

root.mainloop()