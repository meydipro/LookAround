import time
import threading
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    while True:
        time.sleep(1200)  # 20 دقیقه
        messagebox.showinfo("آلارم", "وقت استراحت! لطفاً به اطراف نگاه کنید.")
        time.sleep(20)  # 20 ثانیه
        print("آلارم بعدی برای 20 دقیقه بعد تنظیم شد.")

def start_alarm():
    alarm_thread = threading.Thread(target=set_alarm)
    alarm_thread.start()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("برنامه آلارم")
root.geometry("300x150")

# ایجاد دکمه برای شروع آلارم
start_button = tk.Button(root, text="شروع آلارم", command=start_alarm)
start_button.pack(pady=20)

# اجرای برنامه
root.mainloop()
