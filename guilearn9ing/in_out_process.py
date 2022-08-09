'''testing functions to take input data and then process to give output data'''
from tkinter import *
def get_oc():
    v1= float(volt.get())
    i0 = float(current.get())
    w =float(watt.get())
    voltage_reading = Label(text="The voltage reading is ")
    current_reading = Label(text="the current Ammeter reading is")
    wattmeter_reading = Label(text="the loss wattmeter reading is")
    voltage_reading.pack()
    current_reading.pack()
    wattmeter_reading.pack()
    voltage_entry = Label(textvariable=v1)
    current_entry = Label(textvariable=i0)
    wattage_entry = Label(textvariable=w)
    voltage_entry.pack()
    current_entry.pack()
    wattage_entry.pack()


# Input for open circuit

# def oc_in():
oc_in_frame = Frame()
oc_in_frame.pack()
in_title = Label(oc_in_frame,text="Please enter the test readings", font="ariel 14 bold")
in_title.pack()
voltage_reading = Label(oc_in_frame,text= "Voltmeter reading")
current_reading = Label(oc_in_frame,text="Ammeter reading")
wattmeter_reading=Label(oc_in_frame,text="wattmeter reading")
voltage_reading.pack()
current_reading.pack()
wattmeter_reading.pack()
# voltage_reading.grid(row=1,column=1)
# current_reading.grid(row=2,column=1)
# wattmeter_reading.grid(row=3,column=1)

# Assigning variables
volt = DoubleVar()
current = DoubleVar()
watt = DoubleVar()
 # Code for entrying variables from grid
voltage_entry = Entry(oc_in_frame,textvariable = volt)
current_entry = Entry(oc_in_frame,textvariable = current)
wattage_entry = Entry(oc_in_frame,textvariable = watt)
voltage_entry.pack()
current_entry.pack()
wattage_entry.pack()
# voltage_entry.grid(row=1,column=2)
# current_entry.grid(row=2,column=2)
# wattage_entry.grid(row=3,column=2)
oc_input = Button(oc_in_frame, text="Enter", command=get_oc)
oc_input.pack()
# def print_data():



root= Tk()
# get_oc()
root.mainloop()
