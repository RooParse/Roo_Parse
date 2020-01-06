from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

from mine import *

liscense = '''

This program was created to make tax returns easier and facilitate gathering of data so riders can see what the effects of changes in the algorythms are having on hourly rate over time.

Begin license text.
Copyright 2019 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

End license text.
'''

help_str = '''
1. Slect a folder containing the invoices you wish to parse, it should then show the file path at the bottom of the window. \n

2. Click run to extract the data from the pdfs to csv files. \n

3. Select the folder you wish to save a zip file containing the csv files in, it should then show the file path at the bottom of the window. \n

4. Click save. This will overwrite any folder called "data.zip" in the directory you selected. \n
'''



class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Roo Parse")
        master.configure(background='black')

        self.run_button = Button(master, text="Run", command = lambda: main(self.inv_folder), anchor='w', width=20,justify=LEFT)
        self.run_button.pack(fill=X)    

        self.help_button = Button(master, text="Help", command=self.help,width=20, anchor='w', justify=LEFT)
        self.help_button.pack(fill=X)   

        self.about_button = Button(master, text="About", command=self.about, anchor='w', width=20, justify=LEFT)
        self.about_button.pack(fill=X)   

        self.save_button = Button(master, text="Save", command = lambda: zipdir (self.save_folder,'outputs'), anchor='w', width=20, justify=LEFT)
        self.save_button.pack(fill=X)  

        self.browse_file = Button(master, text="Select invoice folder", command=self.browseFile, anchor='w', width=20, justify=LEFT)
        self.browse_file.pack(fill=X)

        self.save_file = Button(master, text="Select folder to save data", command=self.saveFile, anchor='w', width=20, justify=LEFT)
        self.save_file.pack(fill=X)

        image = Image.open("roo.png")
        photo = ImageTk.PhotoImage(image)

        label = Label(image=photo, borderwidth=0 , highlightthickness=0, relief=None, padx=0,pady=0)
        label.image = photo # keep a reference!
        label.pack()

        self.label_inv = Label(self.master, text="Invoices file path: ", bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_inv.pack(fill=X, side=BOTTOM)

        self.label_save = Label(self.master, text="Save file path: ", bg="black", fg="green", anchor='w', width=20, justify=LEFT)
        self.label_save.pack(fill=X, side=BOTTOM)

        # Text input bar---------------------#
        #self.text = StringVar()
        #self.e = Entry(root, textvariable=self.text)
        #self.e.pack()
        #self.run_button = Button(master, text="Run", command = lambda: main(self.e.get()))
        #self.run_button.pack(fill=X)

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack(fill=X)



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
        messagebox.showinfo("Thank's!", "Data saved to :" + str(self.saveFile) + "\nPlease consider sending in your earnings data, im compiling a database to look into fees over time and i would. All data is anonomous and the source code of this app can be viewed on github. Send it to: email@mail.com")

    def help(self):
        messagebox.showinfo("Help", help_str)

    def about(self):
        messagebox.showinfo("Help", liscense)

root = Tk()
my_gui = GUI(root)
root.mainloop()

