import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        #Create main window
        self.main_window = tkinter.Tk()

        #Create top and bot frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)

        #Create widgets for top frame

        self.label = tkinter.Label(self.top_frame, text='Enter distance in kilometers:')
        self.entry = tkinter.Entry(self.top_frame, width = 10)

        #Pack top frame widgets
        self.label.pack(side='left')
        self.entry.pack(side='left')

        #Create button widgets fro bot frame
        self.cal_btn = tkinter.Button(self.bot_frame,text='Convert',
                                  command=self.convert)
        self.quit_btn = tkinter.Button(self.bot_frame, text='Quit',
                                       command=self.main_window.destroy)

        #Pack the buttons
        self.cal_btn.pack(side='left')
        self.quit_btn.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.bot_frame.pack()

        #Enter tkitner loop
        tkinter.mainloop()

    #Convert func
    def convert(self):
        #Get valute enter by user into the entry widget
        kilo = float(self.entry.get())

        #Convert kilo to miles
        miles = kilo  * 0.6214

        #Display the result in an info dialog box
        tkinter.messagebox.showinfo('Result', str(kilo) +
                                     ' kilometers is equal to ' +
                                     str(miles) + ' miles.')

kilo_conv = KiloConverterGUI()
                                    
