import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):

        #Create main window
        self.main_window = tkinter.Tk()

        #Create top and bot frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bot_frame = tkinter.Frame()

        #Create widgets for top frame

        self.label = tkinter.Label(self.top_frame,
                                   text='Enter distance in kilometers:')
        self.entry = tkinter.Entry(self.top_frame, width = 10)

        #Pack top frame widgets
        self.label.pack(side='left')
        self.entry.pack(side='left')

        #Create widgets for mid frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to miles:')

        #Need a StringVar object to associate with output label
        self.value = tkinter.StringVar()

        #Create label associate with StringVar object
        #Any value stored in StringVar object will display in the label
        self.miles_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.value)

        #Pack the mid frame widgets
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')
        

        #Create button widgets for bot frame
        self.cal_btn = tkinter.Button(self.bot_frame,text='Convert',
                                  command=self.convert)
        self.quit_btn = tkinter.Button(self.bot_frame, text='Quit',
                                       command=self.main_window.destroy)

        #Pack the buttons
        self.cal_btn.pack(side='left')
        self.quit_btn.pack(side='left')

        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

        #Enter tkitner loop
        tkinter.mainloop()

    #Convert func
    def convert(self):
        #Get valute enter by user into the entry widget
        kilo = float(self.entry.get())

        #Convert kilo to miles
        miles = kilo  * 0.6214

        #store value to StringVar object
        self.value.set(miles)

kilo_conv = KiloConverterGUI()
                                    
