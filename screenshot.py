import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import os

class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot App")
        self.root.geometry("400x300")
        
        # Default settings
        self.save_path = os.getcwd()
        self.filename = "screenshot"
        self.format = ".png"
        self.delay = 5
        
        # GUI Elements
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Screenshot Application", font=("Helvetica", 16)).pack(pady=10)

        # Delay input
        tk.Label(self.root, text="Delay (seconds):").pack(pady=5)
        self.delay_entry = tk.Entry(self.root)
        self.delay_entry.insert(0, str(self.delay))
        self.delay_entry.pack()

        # filename input
        tk.Label(self.root, text="Filename:").pack(pady=5)
        self.filename_entry = tk.Entry(self.root)
        self.filename_entry.insert(0, self.filename)
        self.filename_entry.pack()

        # Format dropdown
        tk.Label(self.root, text="Format:").pack(pady=5)
        self.format_var = tk.StringVar(value=self.format)
        tk.OptionMenu(self.root, self.format_var, ".png", ".jpeg", ".bmp").pack()

        # Save path
        tk.Label(self.root, text="Save Path:").pack(pady=5)
        self.path_label = tk.Label(self.root, text=self.save_path, fg="blue")
        self.path_label.pack()
        tk.Button(self.root, text="Select Folder", command=self.choose_directory).pack(pady=5)

        # Buttons for actions
        tk.Button(self.root, text="Capture Full Screen", command=self.capture_full_screen).pack(pady=5)
        tk.Button(self.root, text="Capture Region", command=self.capture_region).pack(pady=5)
    
    def choose_directory(self):
        directory = filedialog.askdirectory(initialdir=self.save_path, title="Select Save Directory")
        if directory:
            self.save_path = directory
            self.path_label.config(text=self.save_path)

    def capture_full_screen(self):
        self.set_delay()
        time.sleep(self.delay)
        screenshot = pyautogui.screenshot()
        self.save_screenshot(screenshot)

    def capture_region(self):
        self.set_delay()
        time.sleep(self.delay)
        messagebox.showinfo("Info", "Drag and select the region to capture.")
        screenshot = pyautogui.screenshot(region=pyautogui.locateOnScreen(pyautogui.screenshot()))
        self.save_screenshot(screenshot)

    def set_delay(self):
        try:
            self.delay = int(self.delay_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid delay value! Using default of 5 seconds.")
            self.delay = 5

    def save_screenshot(self, screenshot):
        filename = self.filename_entry.get() or "screenshot"
        format_ = self.format_var.get()
        full_path = os.path.join(self.save_path, filename + format_)
        try:
            screenshot.save(full_path)
            messagebox.showinfo("Success", f"Screenshot saved to {full_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save screenshot: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()
