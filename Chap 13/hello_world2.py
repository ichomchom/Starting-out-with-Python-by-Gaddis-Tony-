import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create 2 Label widgets contain the text

        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!')

        self.label2 = tkinter.Label(self.main_window,
                                    text = 'This is my GUI program')
        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()

my_gui = MyGUI()        
