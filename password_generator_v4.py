"""
v4 generates a random password from ascii characters adds a weighting system to make letters more
common than numbers and special characters
Adds a gui to make it easier to use
Shows created password in GUI
copies password to clipboard
"""

import pyperclip
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import random


def create_password(password_len):
    # different chars, nums, and symbols that can appear in the password
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    special_characters = '!@#$%^&*()'

    # separate password characters are added into a list once they are generated and join to form a singular string
    password = []

    for i in range(password_len):
        char_decider = random.randint(1, 10)
        if char_decider in range(1, 5):
            char = random.choice(lowercase_letters)
            password.append(char)
        elif char_decider in range(5, 7):
            char = random.choice(uppercase_letters)
            password.append(char)
        elif char_decider in range(7, 9):
            char = random.choice(numbers)
            password.append(char)
        elif char_decider in range(9, 11):
            char = random.choice(special_characters)
            password.append(char)
    # Joins the separate letters in the list together into one singular string
    password_str = "".join(password)
    return password_str


class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Password Length", font=('Calibri', 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, font=('Calibri', 16))
        self.textbox.bind("<Control-Return>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.button = tk.Button(self.root, text="Generate New Password", font=('Calibri', 16),
                                command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.password_label = tk.Label(self.root, text="", font=('Calibri', 16))
        self.password_label.pack(padx=10, pady=10)

        copied_clipboard_font = font.Font(slant="italic")
        self.copied_clipboard = tk.Label(self.root, text="", font=copied_clipboard_font)
        self.copied_clipboard.pack(padx=10, pady=5)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            password_len = int(self.textbox.get('1.0', tk.END))
            if password_len <  100:
                password = create_password(password_len)
                copied_clipboard_text = "password copied to clipboard"
                self.password_label.config(text="Your Password:" + password)
                pyperclip.copy(password)
                self.copied_clipboard.config(text=copied_clipboard_text)

            else:
                quit("Please enter a valid number")

        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        self.show_message()


MyGUI()
