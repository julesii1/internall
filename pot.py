from tkinter import *
import tkinter as trik

def calculate_area():
	aside = float(entry1.get())
	bside = float(entry2.get())
	cside = float(entry3.get())
  perimeter = aside + bside + cside
	output_label.configure(text = ' Perimeter of Triangle= {:.2f} ' .format(area))

def back():
  exec(open('main.py').read())
  exit()

def exit():
   pptriangle_window.destroy()
  
ptriangle_window = trik.Tk()
ptriangle_window.geometry("700x400")
ptriangle_window.config(bg="#c7d6f5")
ptriangle_window.resizable(width=False,height=False)
ptriangle_window.title('Python GUI TUTORIALS')

message_label1 = trik.Label(text= 'Enter a side: ' ,font=( ' Verdana ' , 18))
message_label2 = trik.Label(text= ' Enter b side: ' ,font=( ' Verdana ' , 18))
message_label2 = trik.Label(text= ' Enter c side: ' ,font=( ' Verdana ' , 18))
output_label = trik.Label(font=( ' Verdana ' , 18), text='Area of Triangle is:')
entry1 = trik.Entry(font=( ' Verdana ' , 18), width=6)
entry2 = trik.Entry(font=( ' Verdana ' , 18), width=6)
entry3 = trik.Entry(font=( ' Verdana ' , 18), width=6)
calc_button = trik.Button(text= ' Calculate Area ' , font=( ' Verdana ' , 16),command=calculate_area)
back_button = trik.Button(ptriangle_window,text="Go Back!",font=("Arial",13),command=back)


message_label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)

message_label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)

message_label3.grid(row=3, column=0)
entry3.grid(row=3, column=1)

calc_button.grid(row=1, column=2, rowspan=2)
back_button.grid(row=1, column=4, rowspan=5)
output_label.grid(row=3, column=0, columnspan=3)
mainloop()

