import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def kill_all_pkill():
    os.system(f"pkill -u {os.getlogin()}")
    messagebox.showinfo("Success", "All user processes killed using pkill.")

def kill_all_killall():
    os.system(f"killall -u {os.getlogin()}")
    messagebox.showinfo("Success", "All user processes killed using killall.")

def kill_all_ps_kill():
    user = os.getlogin()
    result = subprocess.run(['ps', '-u', user, '-o', 'pid='], capture_output=True, text=True)
    pids = result.stdout.split()
    for pid in pids:
        os.system(f"kill -9 {pid}")
    messagebox.showinfo("Success", "All user processes killed using ps and kill.")

def kill_all_xkill():
    os.system("xkill")
    messagebox.showinfo("Success", "Click on the windows you want to close.")

def main():
    root = tk.Tk()
    root.title("Kill All Programs")
    root.geometry("500x400")  # Set the size of the window
    root.configure(bg="#0f0f0f")

    label = tk.Label(root, text="Choose a method to kill all programs:", font=("Courier", 16), fg="#00ff00", bg="#0f0f0f")
    label.pack(pady=30)

    button_frame = tk.Frame(root, bg="#0f0f0f")
    button_frame.pack(pady=20)

    button_pkill = tk.Button(button_frame, text="pkill", command=kill_all_pkill, width=20, height=2, bg="#00ff00", fg="#0f0f0f", font=("Courier", 12))
    button_pkill.grid(row=0, column=0, padx=20, pady=10)

    button_killall = tk.Button(button_frame, text="killall", command=kill_all_killall, width=20, height=2, bg="#00ff00", fg="#0f0f0f", font=("Courier", 12))
    button_killall.grid(row=0, column=1, padx=20, pady=10)

    button_ps_kill = tk.Button(button_frame, text="ps and kill", command=kill_all_ps_kill, width=20, height=2, bg="#00ff00", fg="#0f0f0f", font=("Courier", 12))
    button_ps_kill.grid(row=1, column=0, padx=20, pady=10)

    button_xkill = tk.Button(button_frame, text="xkill (for graphical applications)", command=kill_all_xkill, width=20, height=2, bg="#00ff00", fg="#0f0f0f", font=("Courier", 12))
    button_xkill.grid(row=1, column=1, padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
