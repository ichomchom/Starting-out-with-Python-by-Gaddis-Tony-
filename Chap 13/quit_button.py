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

        #Create quit button. When this button clicked
        #the root widget's destroy method is called
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit',
                                          command = self.main_window.destroy)
        
        #Pack the buttons
        self.my_button.pack()
        self.quit_button.pack()
        
        #Enter tkinter mainloop
        tkinter.mainloop()

    #do_something method is a callback function for Button

    def do_something(self):
        #Display info dialog box
        tkinter.messagebox.showinfo('Response', 'Thank for clicking the button.')

my_gui = MyGUI()

