import os
import pygame
from tkinter import filedialog as fd, messagebox as mb
from tkinter import ttk

def show_gif():
    print("gif")

def play_sound():
    pygame.mixer.music.load("./Sounds/file_example_MP3_700KB.mp3")
    pygame.mixer.music.play()

def quit_app(root):
    pygame.mixer.quit()
    root.quit()