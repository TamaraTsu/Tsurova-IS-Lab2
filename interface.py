from tkinter import *

class App:
    def add_list(self):
        for values in range(100):
            self.listbox.insert(END, values)
    def __init__(self):
        self.window = Tk()
        self.window.title("Genetic Algorithm")
        self.window.geometry("500x300")

        # Left frame for information
        self.frame = LabelFrame(self.window, width=200, height=200, bg="skyblue3")
        self.frame.grid(row=0,column=0)
        self.frame.propagate(0)

        # All labels
        self.label1 = Label(self.frame, text='The Best Genes:',
               background="skyblue3").pack(side=TOP, anchor="w")
        self.label2 = Label(self.frame, text='To be or not to be',
                    background="skyblue3").pack(pady=(0,10),side=TOP, anchor="w")

        self.label3 = Label(self.frame, text='Generation' +
                    ' #35',
                    background="skyblue3").pack(side=TOP, anchor="w")

        self.label4 = Label(self.frame, text='Total Population' +
                    ' 600',
                    background="skyblue3").pack(side=TOP, anchor="w")

        self.label5 = Label(self.frame, text='Average fitness :' +
                    '67.89%',
                    background="skyblue3").pack(side=TOP, anchor="w")

        self.label6 = Label(self.frame, text='Max fitness :' +
                    '100%',
                    background="skyblue3").pack(side=TOP, anchor="w")

        self.label7 = Label(self.frame, text='Mutation rate :' +
                    '2.0%',
                    background="skyblue3").pack(side=TOP, anchor="w")
        
        # Right frame for list box
        self.frame2 = LabelFrame(self.window, width=300, height=200, bg="skyblue2")
        self.frame2.grid(row=0,column=1)
        self.frame2.propagate(0)

        self.scrollbar = Scrollbar(self.frame2,orient=VERTICAL)

        self.listbox = Listbox(self.frame2,yscrollcommand= self.scrollbar.set,width=290)
        self.scrollbar.config(command= self.listbox.yview)
        self.scrollbar.pack(side=RIGHT,fill=BOTH)

        self.listbox.pack(side=LEFT,fill=BOTH)

        self.window.mainloop()
        
app = App()