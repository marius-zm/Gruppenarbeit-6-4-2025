import tkinter as tk
from tkinter import ttk
import logic
import pygame

pygame.mixer.init()

root = tk.Tk()
root.title("Button-Tool")
root.geometry("600x300")


def Button(text, command):
    button = ttk.Button(text=text, command=command)
    return button

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frames
top_frame = tk.Frame(root, bg="lightblue", borderwidth=5, relief="solid")
top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_rowconfigure(1, weight=1)
top_frame.grid_columnconfigure(1, weight=1)

bottom_frame = tk.Frame(root, bg="lightblue", borderwidth=5, relief="solid")
bottom_frame.grid(row=1, column=0, sticky="nsew")

# Style
style = ttk.Style()
style.configure('TButton', font=("Arial", 10))
# style.configure('Selected.TButton', font)

# Buttons
show_gif = ttk.Button(top_frame, text="GIF", command=logic.show_gif)
show_gif.grid(row=0, column=0, padx=8, pady=8)

play_sound = ttk.Button(top_frame, text="Play sound", command=logic.play_sound)
play_sound.grid(row=0, column=1, rowspan=2, padx=8, pady=8, sticky="nsew")

quit_app = ttk.Button(bottom_frame, text="Quit", command=lambda: logic.quit_app(root))
quit_app.grid(row=0, column=0)

button3 = ttk.Button(bottom_frame, text="Test")
button3.grid(row=0, column=1)


root.mainloop()
