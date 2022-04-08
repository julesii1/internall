from tkinter import *
import tkinter as trik
import math

def calculate_perimeter():
	radius = float(entry1.get())
	perimeter = 2 * math.pi() * radius
	output_label.configure(text = ' Perimeter of Circle= {:.2f} ' .format(perimeter))

def back():
  exec(open('main.py').read())
  exit()

def exit():
   pcircle_window.destroy()
  
pcircle_window = trik.Tk()
pcircle_window.geometry("700x400")
pcircle_window.config(bg="#c7d6f5")
pcircle_window.resizable(width=False,height=False)
pcircle_window.title('Python GUI TUTORIALS')

message_label1 = trik.Label(text= 'Enter radius: ' ,font=( ' Verdana ' , 18))
output_label = trik.Label(font=( ' Verdana ' , 18), text='Perimeter of Circle is:')
entry1 = trik.Entry(font=( ' Verdana ' , 18), width=6)
calc_button = trik.Button(text= ' Calculate Area ' , font=( ' Verdana ' , 16),command=calculate_perimeter)
back_button = trik.Button(pcircle_window,text="Go Back!",font=("Arial",13),command=back)


message_label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)

calc_button.grid(row=1, column=2, rowspan=2)
back_button.grid(row=1, column=4, rowspan=5)
output_label.grid(row=3, column=0, columnspan=3)
mainloop()

