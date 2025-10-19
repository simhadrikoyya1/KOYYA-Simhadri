import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Emoji Display App")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="😊 Emoji Display App", font=("Arial", 18))
title_label.pack(pady=10)

# Function to display selected emoji
def show_emoji(event):
    selected_emoji = emoji_var.get()
    emoji_label.config(text=selected_emoji, font=("Arial", 80))

# Emoji options
emoji_options = [
    "😀", "😂", "😍", "😎", "😆", "😡", "🤔", "😴", "🥳"
]

# Dropdown menu
emoji_var = tk.StringVar()
emoji_dropdown = ttk.Combobox(root, textvariable=emoji_var, values=emoji_options, font=("Arial", 14))
emoji_dropdown.pack(pady=10)
emoji_dropdown.bind("<<ComboboxSelected>>", show_emoji)

# Label to display emoji
emoji_label = tk.Label(root, text="", font=("Arial", 80))
emoji_label.pack(pady=20)

# Run the app
root.mainloop()
