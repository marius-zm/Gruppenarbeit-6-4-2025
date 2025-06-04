import os
import pygame
import tkinter as tk
from tkinter import filedialog as fd, messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
import random

# Gif
def show_gif():
    gif = tk.Toplevel()
    gif.update()
    width = gif.winfo_width()
    height = gif.winfo_height()
    gif.geometry = (f"{width}x{height}")
    
    label = tk.Label(gif)
    label.grid()

    

    img = Image.open("./Gifs/giphy.gif")

    frames = [
        ImageTk.PhotoImage(frame.copy().convert("RGBA"))
        for frame in ImageSequence.Iterator(img)
    ]

    def update(ind):
        frame = frames[ind]
        label.config(image=frame)
        ind = (ind + 1) % len(frames)
        gif.after(100, update, ind)

    update(0)


# Sound
def play_sound():
    pygame.mixer.music.load("./Sounds/file_example_MP3_700KB.mp3")
    pygame.mixer.music.play()


# Quit
def quit_app(root):
    pygame.mixer.quit()
    root.quit()


# Change color
def change_color(*args):
    color = ["red", "green", "blue", "purple", "orange"]

    for item in args:
        new_color = random.choice(color)
        item.config(bg=new_color)


def change_color_buttons(style):

    styles = [
        {"background": "red", "foreground": "black"},
        {"background": "green", "foreground": "red"},
        {"background": "blue", "foreground": "green"},
        {"background": "orange", "foreground": "yellow"},
    ]
    new_style = random.choice(styles)
    s = new_style

    style.configure(
        "Custom.TButton", background=s["background"], foreground=s["foreground"]
    )
    style.map(
        "Custom.TButton",
        background=[("active", s["background"])],
        foreground=[("active", s["foreground"])],
    )
