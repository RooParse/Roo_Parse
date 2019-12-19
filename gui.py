from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

from mine import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Roo Parse")
        master.configure(background='black')

        s = ttk.Style()
        s.theme_use('alt')
        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack(fill=X)

        self.run_button = Button(master, text="Run", command = lambda: main(self.inv_folder), anchor='w', width=20,justify=LEFT)
        self.run_button.pack(fill=X)    

        self.help_button = Button(master, text="Help", command=self.help,width=20, anchor='w', justify=LEFT)
        self.help_button.pack(fill=X)   

        self.about_button = Button(master, text="About", command=self.about, anchor='w', width=20, justify=LEFT)
        self.about_button.pack(fill=X)   

        self.save_button = Button(master, text="Save", command = lambda: zipdir (self.save_folder,'outputs'), anchor='w', width=20, justify=LEFT)
        self.save_button.pack(fill=X)   

        #self.text = StringVar()
        #self.e = Entry(root, textvariable=self.text)
        #self.e.pack()
        #self.run_button = Button(master, text="Run", command = lambda: main(self.e.get()))
        #self.run_button.pack(fill=X)

        self.browse_file = Button(master, text="Select invoice folder", command=self.browseFile, anchor='w', width=20, justify=LEFT)
        self.browse_file.pack(fill=X)

        self.save_file = Button(master, text="Select folder to save data", command=self.saveFile, anchor='w', width=20, justify=LEFT)
        self.save_file.pack(fill=X)

        self.label_inv = Label(self.master, text="Invoices file path: ", bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_inv.pack(fill=X, side=TOP)

        self.label_save = Label(self.master, text="Save file path: ", bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_save.pack(fill=X, side=TOP)

        image = Image.open("roo.png")
        photo = ImageTk.PhotoImage(image)

        label = Label(image=photo, borderwidth=0 , highlightthickness=0, relief=None, padx=0,pady=0)
        label.image = photo # keep a reference!
        label.pack()


    def browseFile(self):
        self.label_inv.destroy()
        self.inv_folder = askdirectory()
        self.label_inv = Label(self.master, text="Invoices file path: " + self.inv_folder, bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_inv.pack(fill=X, side=BOTTOM)

    def saveFile(self):
        self.label_save.destroy()
        self.save_folder = askdirectory()
        self.label_save = Label(self.master, text="Save file path: " + self.save_folder, bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_save.pack(fill=X, side=BOTTOM)

    def help(self):
        messagebox.showinfo("Help", "Email: \n Github: \n")

    def about(self):
        messagebox.showinfo("Help", "Email: \n Github: \n")

root = Tk()
my_gui = GUI(root)
root.mainloop()

