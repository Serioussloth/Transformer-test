'''just trying to add image to canvas to see if can shrink the size of image '''
from tkinter import *
open_photo = PhotoImage(file='open circuit test img.png')
width = 1280
height = 720
root = Tk()
root.geometry(f"{width}x{height}")
can_img = Canvas(root, width = width , height= height)
can_img.create_image(image = open_photo)
root.mainloop()