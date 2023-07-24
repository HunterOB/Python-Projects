

import tkinter_password_generator as tk
import random
from tkinter import messagebox

root = tk.Tk()

root.geometry("500x500")
root.title("Password Generator V3")

label = tk.Label(root, text="Please enter password length", font=('Calibri', 18))
label.pack(padx=20, pady=(30,10))

textbox = tk.Text(root, height=1, font=('Calibri', 16))
textbox.pack(padx=50)

button = tk.Button(root, text="Confirm", font=('Calibri', 16))
button.pack(pady=15)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=10)
buttonframe.columnconfigure(1, weight=10)

btn1 = tk.Button(buttonframe, text="Yes", font=('Calibri', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=(15, 7.5))

btn2 = tk.Button(buttonframe, text="No", font=('Calibri', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=(7.5, 15))
buttonframe.pack(fill='x')

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Password Length", font=('Calibri', 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=1, font=('Calibri', 16))
        self.textbox.bind("<Control-Return>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.button = tk.Button(self.root, text="Show Message",  font=('Calibri', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        self.show_message()





root.mainloop()

