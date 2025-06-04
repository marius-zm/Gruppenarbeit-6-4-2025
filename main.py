import tkinter as tk
from tkinter import ttk
import logic
import pygame

pygame.mixer.init()

theme = "lightblue"

root = tk.Tk()
root.title("Button-Tool")
root.geometry("600x300")
root.config(bg=theme)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frames
top_frame = tk.Frame(root, bg=theme, borderwidth=5, relief="solid")
top_frame.grid(row=0, column=0, columnspan=3, sticky="nsew")
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid_rowconfigure(1, weight=1)
top_frame.grid_columnconfigure(1, weight=1)

bottom_frame = tk.Frame(root, bg=theme, borderwidth=5, relief="solid")
bottom_frame.grid(row=1, column=0, sticky="nsew")

# Style
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 10))
# style.configure('Selected.TButton', font)

# Buttons
show_gif = ttk.Button(top_frame, text="GIF", command=logic.show_gif, style="Custom.TButton")
show_gif.grid(row=0, column=0, padx=8, pady=8)

play_sound = ttk.Button(top_frame, text="Play sound", command=logic.play_sound, style="Custom.TButton")
play_sound.grid(row=0, column=1, rowspan=2, padx=8, pady=8, sticky="nsew")

quit_app = ttk.Button(bottom_frame, text="Quit", command=lambda: logic.quit_app(root), style="Custom.TButton")
quit_app.grid(row=0, column=0)

change_color_frames = ttk.Button(bottom_frame, text="Rainbow", command=lambda: logic.change_color(top_frame, bottom_frame), style="Custom.TButton")
change_color_frames.grid(row=0, column=1)

change_color_buttons = ttk.Button(bottom_frame, text="Rainbow Buttons", command=lambda: logic.change_color_buttons(style), style="Custom.TButton")
change_color_buttons.grid(row=0, column=2)


root.mainloop()
