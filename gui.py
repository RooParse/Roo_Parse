from tkinter import *
from PIL import Image, ImageTk

from mine import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Roo Parse")
        
        #img = ImageTk.PhotoImage(Image.open())

        self.label = Label(master, text="Roo Parse")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.run_button = Button(master, text="Run", command = lambda: main(self.e.get()))
        self.run_button.pack()       

        self.help_button = Button(master, text="Help", command=main)
        self.help_button.pack()   

        self.about_button = Button(master, text="About", command=main)
        self.about_button.pack()   

        self.label = Label(master, text="Invoices file path: ")
        self.label.pack()

        self.text = StringVar()
        self.e = Entry(root, textvariable=self.text)
        self.e.pack()

        self.greet_button = Button(master, text="Save", command=self.save_text)
        self.greet_button.pack()

    def save_text(self):
        self.path = self.e.get()
        print(self.text)
        return self.text

root = Tk()
my_gui = GUI(root)
root.mainloop()

