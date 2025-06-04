import tkinter as tk
from tkinter import ttk
import random

def start_game():
    game_win = tk.Toplevel()
    game_win.title("🪨 Stein - ✂️ Schere - 📄 Papier")
    game_win.geometry("400x300")

    options = {
        "Stein": "🪨",
        "Schere": "✂️",
        "Papier": "📄"
    }

    def scissors(choice_player):
        choice_enemy = random.choice(list(options.keys()))
        if choice_player == choice_enemy:
            result = "Unentschieden!"
        elif (choice_player == "Stein" and choice_enemy == "Schere") or \
             (choice_player == "Schere" and choice_enemy == "Papier") or \
             (choice_player == "Papier" and choice_enemy == "Stein"):
            result = "Du gewinnst!"
        else:
            result = "Du verlierst!"

        enemy_label.config(text=f"Gegner: {options[choice_enemy]}")
        result_label.config(text=result)

    main_frame = ttk.Frame(game_win)
    main_frame.pack(padx=20, pady=20)

    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=0, column=0, sticky="n")

    style = ttk.Style(game_win)
    style.configure("Emoji.TButton", font=("Arial", 16), padding=10)

    for i, choice in enumerate(options):
        ttk.Button(button_frame, text=options[choice], style="Emoji.TButton",
                   command=lambda w=choice: scissors(w)).grid(row=i, column=0, pady=5)

    output_frame = ttk.Frame(main_frame)
    output_frame.grid(row=0, column=1, padx=20, sticky="n")

    enemy_label = ttk.Label(output_frame, text="Gegner: ❓", font=("Arial", 16))
    enemy_label.pack(pady=10)

    result_label = ttk.Label(output_frame, text="", font=("Arial", 16))
    result_label.pack(pady=10)