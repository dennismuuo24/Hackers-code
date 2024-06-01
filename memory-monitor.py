import psutil
import tkinter as tk
from tkinter import ttk

class MonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Monitor")

        self.cpu_frame = ttk.LabelFrame(root, text="CPU Usage")
        self.cpu_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        self.cpu_label = ttk.Label(self.cpu_frame, text="")
        self.cpu_label.grid(row=0, column=0, padx=10, pady=5)

        self.memory_frame = ttk.LabelFrame(root, text="Memory Usage")
        self.memory_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        self.memory_label = ttk.Label(self.memory_frame, text="")
        self.memory_label.grid(row=0, column=0, padx=10, pady=5)

        self.disk_frame = ttk.LabelFrame(root, text="Disk Usage")
        self.disk_frame.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        self.disk_label = ttk.Label(self.disk_frame, text="")
        self.disk_label.grid(row=0, column=0, padx=10, pady=5)

        self.network_frame = ttk.LabelFrame(root, text="Network Activity")
        self.network_frame.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        self.network_label = ttk.Label(self.network_frame, text="")
        self.network_label.grid(row=0, column=0, padx=10, pady=5)

        self.update_labels()

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        network_io = psutil.net_io_counters()

        self.cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        self.memory_label.config(text=f"Total Memory: {self.bytes_to_gb(mem.total)} GB, Available: {self.bytes_to_gb(mem.available)} GB")
        self.disk_label.config(text=f"Total Disk: {self.bytes_to_gb(disk_usage.total)} GB, Used: {self.bytes_to_gb(disk_usage.used)} GB")
        self.network_label.config(text=f"Bytes Sent: {self.bytes_to_gb(network_io.bytes_sent)} GB, Bytes Received: {self.bytes_to_gb(network_io.bytes_recv)} GB")

        self.root.after(1000, self.update_labels)

    def bytes_to_gb(self, bytes):
        return round(bytes / (1024 ** 3), 2)

def main():
    root = tk.Tk()
    app = MonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
