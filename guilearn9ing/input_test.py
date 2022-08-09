'''Just checking if inputs and its calculations work or not'''
from tkinter import *
from math import *
def oc_calulations():
    v0 = float(input("enter OC voltage"))
    i0 = float(input("enter oc current"))
    w0 = float(input("enter oc loss"))
    i1 = float(input("enter SC current"))
    v1 = float(input("enter SC voltage"))
    w1 = float(input("enter SC loss"))
    iw = w0/v0
    r0 = v0/iw  # winding resistance
    x0 = v0/sqrt(i0*i0-iw*iw)  # winding impedance
    r01 = pow(i1,2)/w1
    z01 = v1/i1
    x01 = sqrt(z01*z01-r01*r01)
    print("The parameters of the transformers are --> \n")
    print("R0 = %.2f"%r0)
    print("X0 = %.2f"%x0)
    print("R01 = %.2f"%r01)
    print("X01 = %.2f"%x01)

oc_calulations()
