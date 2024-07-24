import tkinter as tk

class Mycalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x500")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP02", font=('Ariel', 20))
        self.label.pack()

        self.button = tk.Button(self.root, text='CLICK HERE', height=5)
        self.button.place(x=0, y=50)
        
    

        self.root.mainloop()

Mycalculator()