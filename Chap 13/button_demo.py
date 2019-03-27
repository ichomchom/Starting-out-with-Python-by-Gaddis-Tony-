import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        #Create main window
        self.main_window = tkinter.Tk()

        #Create button, with text 'Click Me!'
        #do_something method should executed when user clicks the Buttons
        self.my_button = tkinter.Button(self.main_window, text = 'Click Me!',
                                        command = self.do_something)

        #Pack the button
        self.my_button.pack()

        #Enter tkinter mainloop
        tkinter.mainloop()

    #do_something method is a callback function for Button

    def do_something(self):
        #Display info dialog box
        tkinter.messagebox.showinfo('Response', 'Thank for clicking the button.')

my_gui = MyGUI()
