'''same as emtestbody just with class'''
'''This is first tkinter program'''
from tkinter import *
from math import *
from PIL import Image, ImageTk


class transtest:
    def __init__(self):
        root = Tk()
        root.geometry("1280x720")
        root.title("Just first test")
        # root.maxsize(1152, 648)
        root.minsize(160, 90)
        op = Image.open("open circuit test img.png")
        op = op.resize((520, 200), Image.ANTIALIAS)
        sp = Image.open("short circuit test img.png")
        sp = sp.resize((520, 200), Image.ANTIALIAS)
        open_photo = ImageTk.PhotoImage(op)
        short_photo = ImageTk.PhotoImage(sp)
        self.volt = DoubleVar()
        self.current = DoubleVar()
        self.watt = DoubleVar()
        self.sc_volt = DoubleVar()
        self.sc_current = DoubleVar()
        self.sc_watt = DoubleVar()
        self.iw = DoubleVar()
        self.r0 = DoubleVar()
        self.x0 = DoubleVar()
        self.r01 = DoubleVar()
        self.x01 = DoubleVar()
        self.z01 =DoubleVar()
        # INTRO part of progarm
# frame 1
        intro = Frame(root, bg="green")
        intro.pack(side="top")
        intro_text = Label(intro, text="Welcome to the Open and Short Circuit test.", font="ariel 18 bold")
        intro_text.pack(side="top", anchor="nw")

        # Open circuit test skeleton
# FRame 2
        open_test_intro = Frame(root, borderwidth=5, relief=RAISED, width=900, height=200)
        open_test_intro.pack(anchor="n", fill="x")
        open_test_heading = Label(open_test_intro, text='''Please enter the values for the 
        open circuit test. The current, voltage and wattmeter readings
         are standard marked in the given below diagram''', bg="grey",
                                  font="timesnewroman 10 bold", borderwidth=5, relief=SUNKEN, padx=5, pady=10,
                                  justify="left")

        open_test_heading.pack(side="top", anchor="nw")
        open_photo_label = Label(open_test_intro, image=open_photo)
        open_photo_label.pack(side="left", pady=5)

        oc_in_frame = Frame(open_test_intro)
        oc_in_frame.pack(side="right", pady=(0, 70))
        in_title = Label(oc_in_frame, text="Please enter the open test readings", font="ariel 14 bold")
        in_title.pack()
        voltage_reading = Label(oc_in_frame, text="Voltmeter reading")
        current_reading = Label(oc_in_frame, text="Ammeter reading")
        wattmeter_reading = Label(oc_in_frame, text="wattmeter reading")
        # voltage_reading.grid(row=1,column=1)
        # current_reading.grid(row=2,column=1)
        # wattmeter_reading.grid(row=3,column=1)

        # Assigning variables

        # Code for entrying variables from grid
        voltage_entry = Entry(oc_in_frame, textvariable=self.volt)
        current_entry = Entry(oc_in_frame, textvariable=self.current)
        wattage_entry = Entry(oc_in_frame, textvariable=self.watt)
        voltage_reading.pack()
        voltage_entry.pack()
        current_reading.pack()
        current_entry.pack()
        wattmeter_reading.pack()
        wattage_entry.pack()
        # voltage_entry.grid(row=1,column=2)
        # current_entry.grid(row=2,column=2)
        # wattage_entry.grid(row=3,column=2)
        # oc_input = Button(oc_in_frame, text="Enter", command=get_oc)
        # oc_input.pack()

        # this is the code for entering data

        # Input for open circuit
        # def oc_in():

        # Short circuit test skeleton


# Frame 3
        short_test_intro = Frame(root, borderwidth=5, relief=RAISED, width=900, height=200)
        short_test_intro.pack(anchor="n", fill="x")
        short_test_heading = Label(short_test_intro, text='''Please enter the values for the 
        short circuit test. The current,voltage and wattmeter readings
         are standard marked in the given below diagram''', bg="grey",
                                   font="timesnewroman 10 bold", borderwidth=5, relief=SUNKEN, padx=5, pady=10,
                                   justify="left")

        short_test_heading.pack(side="top", anchor="nw")
        short_photo_label = Label(short_test_intro, image=short_photo)
        short_photo_label.pack(side="left", pady=5, anchor="ne")

        oc_in_frame = Frame(short_test_intro)
        oc_in_frame.pack(side="right", pady=(0, 70))
        in_title = Label(oc_in_frame, text="Please enter the open test readings", font="ariel 14 bold")
        in_title.pack()
        sc_voltage_reading = Label(oc_in_frame, text="Voltmeter reading")
        sc_current_reading = Label(oc_in_frame, text="Ammeter reading")
        sc_wattmeter_reading = Label(oc_in_frame, text="wattmeter reading")
        # voltage_reading.grid(row=1,column=1)
        # current_reading.grid(row=2,column=1)
        # wattmeter_reading.grid(row=3,column=1)

        # Assigning variables

        # Code for entrying variables from grid
        sc_voltage_entry = Entry(oc_in_frame, textvariable=self.sc_volt)
        sc_current_entry = Entry(oc_in_frame, textvariable=self.sc_current)
        sc_wattage_entry = Entry(oc_in_frame, textvariable=self.sc_watt)
        sc_voltage_reading.pack()
        sc_voltage_entry.pack()
        sc_current_reading.pack()
        sc_current_entry.pack()
        sc_wattmeter_reading.pack()
        sc_wattage_entry.pack()
        # voltage_entry.grid(row=1,column=2)
        # current_entry.grid(row=2,column=2)
        # wattage_entry.grid(row=3,column=2)
        # TODO: add a function to input the data
        # oc_input = Button(oc_in_frame, text="Enter", command=get_sc)
        # oc_input.pack()

        # CALCULATION OF THE DATA AND DISPLAYING OUTPUT
        def calculation():
            v0 = self.volt.get()
            i0 = self.current.get()
            w0 = self.watt.get()
            # print("Open Voltage = {0} \n Open Current = {1}\nOpen WAttage = {2}".format(v0, i0, w0))
            v1 = self.sc_volt.get()
            i1 = self.sc_current.get()
            w1 = self.sc_watt.get()
            # print("Short Voltage = {0} \nShort Current = {1}\nShort WAttage = {2}".format(v1, i1, w1))
            iw = w0 / v0
            r0 = v0 / iw  # winding resistance
            x0 = v0 / sqrt(i0 * i0 - iw * iw)  # winding impedance
            r01 = w1/pow(i1, 2)
            z01 = v1 / i1
            x01 = sqrt(z01 * z01 - r01 * r01)
            # if self.volt == 0 or self.current == 0 or self.watt == 0 or self.sc_volt == 0 or self.sc_current == 0 or \
            #         self.sc_watt == 0:
            #     Entry(root, text="Please enter all the variables." ,font="ariel 14 bold").pack()
            #
            print("The parameters of the transformers are --> \n")
            print("R0 = %.2f" % r0)
            print("X0 = %.2f" % x0)
            print("R01 = %.2f" % r01)
            print("X01 = %.2f" % x01)

            showoutput = Tk()
            showoutput.geometry("400x200")
            ouput_label = Frame(showoutput)
            Label(ouput_label, text= "The parallel resistance, R0 =  %.2f"% r0).pack()
            Label(ouput_label, text= "The parallel reactance, X0 =  %.2f"% x0).pack()
            Label(ouput_label, text= "The equivalent higher side resistance, R01 =  %.2f"% r01).pack()
            Label(ouput_label, text= "The equivalent higher side reactance, X01 =  %.2f"% x01).pack()
            Button(ouput_label, text="New test?", )
            ouput_label.pack()
            showoutput.mainloop()



        calc = Button(oc_in_frame, text="Show output", command=calculation)
        calc.pack()

        #
        # # Button for open circuit enabling
        # oc_button = Button(intro,text= "Open circuit test",command=oc)
        # oc_button.pack(side="left",fill="x")
        #
        # # Button for short circuit enabling
        # sc_button = Button(intro,text= "short circuit ",command=sc)
        # sc_button.pack(side="left",fill="x")

        root.mainloop()


transtest()
