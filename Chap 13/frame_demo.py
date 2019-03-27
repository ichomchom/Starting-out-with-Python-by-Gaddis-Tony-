import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create two frames, one on top, on on bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        #Create 3 Labels for top frame
        self.label1 = tkinter.Label(self.top_frame, text='Winken')
        self.label2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label3 = tkinter.Label(self.top_frame, text='Nod')

        #Pack the labels in top frame
        #Use the side='top' argument to stack them on top of each other
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        #Create three labels for bot frame
        self.label4 = tkinter.Label(self.bot_frame, text='Winken')
        self.label5 = tkinter.Label(self.bot_frame, text='Blinken')
        self.label6 = tkinter.Label(self.bot_frame, text='Nod')

        #Pack the labels in bot frame
        #Use the side='lef' argument to stack them on top of each other
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.bot_frame.pack()

        #Enter the tkinter main loop
        tkinter.mainloop()

my_gui = MyGUI()        
