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
    gif.title("GIF Viewer")
    gif.geometry("400x300")  # Startgröße

    label = tk.Label(gif, bg="black")
    label.pack(fill="both", expand=True)

    # Lade das GIF
    img = Image.open("./Gifs/giphy.gif")
    frames = [frame.copy().convert("RGBA") for frame in ImageSequence.Iterator(img)]

    # Erzeuge Originalgrößen für spätere Skalierung
    original_frames = frames.copy()

    def update(ind):
        frame = original_frames[ind]

        # Hol aktuelle Größe des Fensters
        width = label.winfo_width()
        height = label.winfo_height()

        # Skaliere Frame auf Fenstergröße (ohne Seitenverhältnis)
        resized = frame.resize((width, height), Image.Resampling.LANCZOS)
        tk_frame = ImageTk.PhotoImage(resized)

        label.img = tk_frame  # Verhindere Garbage Collection
        label.config(image=tk_frame)

        next_ind = (ind + 1) % len(original_frames)
        gif.after(100, update, next_ind)

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
