import tkinter

class Store:
    def __init__(self):
        self.variable = tkinter.IntVar()

    def add(self, value):
        var = self.variable
        var.set(var.get() + value)
        return var.get()

class Main(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        var = Store()
        self.label  = tkinter.Label(self, textvariable=var.variable)
        self.button = tkinter.Button(self, command=lambda: var.add(1), text='+1')
        self.label.pack()
        self.button.pack()


root = Main()
root.mainloop()