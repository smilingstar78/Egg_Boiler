import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
from PIL import Image, ImageTk

# Countdown time (in seconds)
TAKING_OUT = 5 * 60  # 5 minutes

def start_timer():
    def countdown():
        remaining = TAKING_OUT
        while remaining > 0:
            mins, secs = divmod(remaining, 60)
            timer_label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            remaining -= 1
        timer_label.config(text="00:00")
        messagebox.showinfo("Egg Timer", "🥚 Take out the egg!!!")

    # Start countdown in separate thread so GUI doesn’t freeze
    Thread(target=countdown).start()

# GUI setup
root = tk.Tk()
root.title("🥚 Egg Boiling Timer")
root.geometry("500x400")

# Load background image (cute egg wallpaper!)
# Make sure to have an image file named 'eggs.jpg' in the same folder!
try:
    bg_image = Image.open("eggs.jpg")
    bg_image = bg_image.resize((500, 400), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="lightyellow")  # fallback background

# Timer display
timer_label = tk.Label(root, text="05:00", font=("Helvetica", 48, "bold"), bg="white", fg="#222")
timer_label.place(relx=0.5, rely=0.4, anchor="center")

# Start button
start_button = tk.Button(root, text="Start Boiling 🍳", font=("Helvetica", 16), command=start_timer, bg="#ffeb99", fg="#333", padx=10, pady=5)
start_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
