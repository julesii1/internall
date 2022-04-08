from tkinter import *
import tkinter as trik

def calculate_perimeter():
	base = float(entry1.get())
	height = float(entry2.get())
	perimeter = (base + height) * 2
	output_label.configure(text = ' Perimeter of Square= {:.2f} ' .format(perimeter))

def back():
  exec(open('main.py').read())
  exit()

def exit():
   psquare_window.destroy()
  
psquare_window = trik.Tk()
psquare_window.geometry("700x400")
psquare_window.config(bg="#c7d6f5")
psquare_window.resizable(width=False,height=False)
psquare_window.title('Python GUI TUTORIALS')

message_label1 = trik.Label(text= 'Enter base: ' ,font=( ' Verdana ' , 18))
message_label2 = trik.Label(text= ' Enter height: ' ,font=( ' Verdana ' , 18))
output_label = trik.Label(font=( ' Verdana ' , 18), text='Perimter of Square is:')
entry1 = trik.Entry(font=( ' Verdana ' , 18), width=6)
entry2 = trik.Entry(font=( ' Verdana ' , 18), width=6)
calc_button = trik.Button(text= ' Calculate Area ' , font=( ' Verdana ' , 16),command=calculate_perimeter)
back_button = trik.Button(psquare_window,text="Go Back!",font=("Arial",13),command=back)


message_label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)

message_label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)

calc_button.grid(row=1, column=2, rowspan=2)
back_button.grid(row=1, column=4, rowspan=5)
output_label.grid(row=3, column=0, columnspan=3)
mainloop()

