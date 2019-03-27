import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create a Label widget contain the text
        #'Hello World!'
        self.label = tkinter.Label(self.main_window, text = 'Hello World!')

        self.label.pack()

        tkinter.mainloop()

my_gui = MyGUI()        
