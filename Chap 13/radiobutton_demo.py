import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create 2 frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        #Create IntVar obj to use with Radiobutton
        self.radio_var = tkinter.IntVar()

        #Set the intVar obj to 1
        self.radio_var.set(1)

        #Create Radiobutton widgets in top frames
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Option 3',
                                       variable=self.radio_var,
                                       value=3)

        #Pack Radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

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
        tkinter.messagebox.showinfo('Selection', 'You selected option ' +
                                     str(self.radio_var.get()))

my_gui = MyGUI()
