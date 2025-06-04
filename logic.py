import os
import pygame
import tkinter as tk
from tkinter import filedialog as fd, messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence

# Gif

def show_gif():
    gif = tk.Toplevel()
    gif.geometry("600x300")
    
    label = tk.Label(gif)
    label.grid()

    img = Image.open("./Gifs/giphy.gif")

    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(img)]

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