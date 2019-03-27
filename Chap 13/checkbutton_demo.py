import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create 2 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        #Create IntVar obj to use with Checkbuttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        #Set the intVar obj to 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        #Create Radiobutton widgets in top frames
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.cb_var3)

        #Pack Radiobuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #Create OK btn and Quit btn
        self.ok_btn = tkinter.Button(self.bot_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_btn = tkinter.Button(self.bot_frame,
                                       text='Quit',
                                       command=self.main_window.destroy)

        #Pack the buttons
        self.ok_btn.pack(side='left')
        self.quit_btn.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.bot_frame.pack()

        #Start mainloop
        tkinter.mainloop()

    #Show_choice method for OK button
    def show_choice(self):
        #Create a message string.
        self.message = 'You selected:\n'

        #Determine which Checkbuttons are seletected
        #and build the message string accordingly
        if self.cb_var1.get() == 1:
            self.message = self.message + '1\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '2\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '3\n'
            
        tkinter.messagebox.showinfo('Selection', self.message)

my_gui = MyGUI()
