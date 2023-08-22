#creating a basic calculator application that can perform add, subtract, multiply and divide operation using python and tkinter for the gui

import tkinter as tk

class Calculator_App: 
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")

        #number display section 
        self.entry = tk.Entry(root, width=20, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=4)

        #button declaration 
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("All Clear", 5, 0)
        ]

        #create buttons

        self.buttons = []

        for label, row , col in buttons:
            button = self.create_button(label, row, col)
            self.buttons.append(button)

    def create_button(self, label, row, col):
        if(label!="All Clear"):
            button = tk.Button(self.root, text=label, width=5, height=2, font=("Helvetica", 15), command=lambda: self.on_button_click(label))
            button.grid(row=row, column=col)
        else:
            button = tk.Button(self.root, text=label, width=15, height=2, font=("Helvetica", 15), command=lambda: self.all_clear(label))
            button.grid(row=row, column=col, columnspan=4)
        return button
    
    def on_button_click(self, label):
        if label == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + label)

    def all_clear(self,label):
        if label == "All Clear":
            self.entry.delete(0, tk.END)


root = tk.Tk()
app = Calculator_App(root)
root.mainloop()

        



