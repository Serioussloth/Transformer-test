'''This is first tkinter program'''
from tkinter import *
root = Tk()
root.geometry("1280x720")
root.title("Just first test")
# root.maxsize(1152, 648)
root.minsize(160, 90)
open_photo = PhotoImage(file='open circuit test img.png')
short_photo = PhotoImage(file = 'short circuit test img.png')

# Open circuit test skeleton

def oc():

    def get_oc():
        v1 = volt.get()
        i0 = current.get()
        w = watt.get()
        # print("Voltage = {0} \nCurrent = {1}\nWAttage = {2}".format(v1, i0, w))

    open_test_intro = Frame(root, borderwidth=5, relief=RAISED )
    open_test_intro.pack(anchor="n",fill= "x" )
    open_test_heading = Label( open_test_intro,text='''Please enter the values for the 
    open circuit test. The current, voltage and wattmeter readings
     are standard marked in the given below diagram''', bg="grey",
                              font="timesnewroman 10 bold", borderwidth=5, relief=SUNKEN, padx=5, pady=10,
                              justify = "left")

    open_test_heading.pack(side = "top",anchor="nw")
    open_photo_label = Label(open_test_intro,image = open_photo)
    open_photo_label.pack(side="right", pady=5)

    oc_in_frame = Frame(open_test_intro)
    oc_in_frame.pack(side="left" )
    in_title = Label(oc_in_frame, text="Please enter the open test readings", font="ariel 14 bold")
    in_title.pack()
    voltage_reading = Label(oc_in_frame, text="Voltmeter reading")
    current_reading = Label(oc_in_frame, text="Ammeter reading")
    wattmeter_reading = Label(oc_in_frame, text="wattmeter reading")
    # voltage_reading.grid(row=1,column=1)
    # current_reading.grid(row=2,column=1)
    # wattmeter_reading.grid(row=3,column=1)

    # Assigning variables
    volt = DoubleVar()
    current = DoubleVar()
    watt = DoubleVar()
    # Code for entrying variables from grid
    voltage_entry = Entry(oc_in_frame, textvariable=volt)
    current_entry = Entry(oc_in_frame, textvariable=current)
    wattage_entry = Entry(oc_in_frame, textvariable=watt)
    voltage_reading.pack()
    voltage_entry.pack()
    current_reading.pack()
    current_entry.pack()
    wattmeter_reading.pack()
    wattage_entry.pack()
    # voltage_entry.grid(row=1,column=2)
    # current_entry.grid(row=2,column=2)
    # wattage_entry.grid(row=3,column=2)
    oc_input = Button(oc_in_frame, text="Enter", command=get_oc)
    oc_input.pack()

    # this is the code for entering data

# Input for open circuit
# def oc_in():




# Short circuit test skeleton

def sc():

    def get_sc():
        V = sc_volt.get()
        I = sc_current.get()
        W = sc_watt.get()
        # print("Voltage = {0} \nCurrent = {1}\nWAttage = {2}".format(v1, i0, w))


    short_test_intro = Frame(root, borderwidth=5, relief=RAISED)
    short_test_intro.pack(anchor="n", fill="x")
    short_test_heading = Label(short_test_intro, text='''Please enter the values for the 
    short circuit test. The current,voltage and wattmeter readings
     are standard marked in the given below diagram''', bg="grey",
                              font="timesnewroman 10 bold", borderwidth=5, relief=SUNKEN, padx=5, pady=10,
                               justify = "left")

    short_test_heading.pack(side = "top",anchor = "nw")
    short_photo_label = Label(short_test_intro, image=short_photo)
    short_photo_label.pack(side="right", pady=5,anchor="ne")

    oc_in_frame = Frame(short_test_intro)
    oc_in_frame.pack(side="left")
    in_title = Label(oc_in_frame, text="Please enter the open test readings", font="ariel 14 bold")
    in_title.pack()
    sc_voltage_reading = Label(oc_in_frame, text="Voltmeter reading")
    sc_current_reading = Label(oc_in_frame, text="Ammeter reading")
    sc_wattmeter_reading = Label(oc_in_frame, text="wattmeter reading")
    # voltage_reading.grid(row=1,column=1)
    # current_reading.grid(row=2,column=1)
    # wattmeter_reading.grid(row=3,column=1)

    # Assigning variables
    sc_volt = DoubleVar()
    sc_current = DoubleVar()
    sc_watt = DoubleVar()
    # Code for entrying variables from grid
    sc_voltage_entry = Entry(oc_in_frame, textvariable=sc_volt)
    sc_current_entry = Entry(oc_in_frame, textvariable=sc_current)
    sc_wattage_entry = Entry(oc_in_frame, textvariable=sc_watt)
    sc_voltage_reading.pack()
    sc_voltage_entry.pack()
    sc_current_reading.pack()
    sc_current_entry.pack()
    sc_wattmeter_reading.pack()
    sc_wattage_entry.pack()
    # voltage_entry.grid(row=1,column=2)
    # current_entry.grid(row=2,column=2)
    # wattage_entry.grid(row=3,column=2)
    oc_input = Button(oc_in_frame, text="Enter", command=get_sc)
    oc_input.pack()




# INTRO part of progarm
intro = Frame(root, bg = "green")
intro.pack(side="top")
intro_text = Label(intro, text= "Welcome to the Open and Short Circuit test.")
intro_text.pack(side="top",anchor="nw")
oc()
sc()
#
# # Button for open circuit enabling
# oc_button = Button(intro,text= "Open circuit test",command=oc)
# oc_button.pack(side="left",fill="x")
#
# # Button for short circuit enabling
# sc_button = Button(intro,text= "short circuit ",command=sc)
# sc_button.pack(side="left",fill="x")

root.mainloop()
