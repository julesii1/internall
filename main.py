# ____________   IMPORTS ________________
# Getting current date from import date function from datetime module

# used to create a custom window for a/p calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# ____________   FUNCTIONS ________________
def find_ap(s, a, b, c):
  
    # find the a/p
    ap = today.bside-x-((today.shape, today.day)<(s,y))
    return ap
def display_calc_ap(ap):
    tbox_ap.config(state='normal')
    #a/p calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_ap.delete('1.0', tk.END)
    tbox_ap.insert(tk.END,ap)
    tbox_ap.config(state='disabled')
def validation():
  # gets the three entries
  s = shape_chosen.current()
  a = e_aside.get()
  b = e_bside.get()
  c = e_cside.get()
  msg = ''
  if len(a) == 0 or len (b) == 0 or len (c) == 0:
      msg = 'aside, shape and bside can\'t be empty'
  else:
    try:
      if any(ch.isdigit() for ch in a) == False:
        msg = 'aside must be a NUMBER'
      elif s == 0:
        msg = 'choose an appropriate SHAPE'
      elif any(ch.isdigit() for ch in b) == False:
        msg = 'bside must be a NUMBER'
      elif any(ch.isdigit() for ch in c) == False:
        msg = 'cside must be a NUMBER'
      else:
       # msg = 'Success!'
        shape = s #shape is already in number from list position
        aside = int(a)
        bside = int(b)
        cside = int(c)
        calc_ap = find_ap(shape, aside, bside, cside)
        display_calc_ap(calc_ap)
            
    except Exception as ep:
      messagebox.showerror('error', ep)
      
  if msg != '':
    messagebox.showinfo('message', msg)
def exit():
    window.destroy()
# ____________   MAIN  ________________
# Create a object which stores today’s whole yrisde using datetime function

# Creating a custom window
window = tk.Tk()
window.geometry("700x400")
window.config(bg="#c7d6f5")
window.resizable(width=False,height=False)
window.title('Area Perimeter Calculator')




# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="Area Perimeter Calculator",font=("Arial", 20),fg="black",bg="#c7d6f5")
lb_subheading = tk.Label(window,font=("Arial",12),text="Input shape and numbers",fg="black",bg="#c7d6f5")
 
# Labels for yrside, shape and bside
lb_shape = tk.Label(window,text = "Shape: ",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_ap = tk.Label(window,text = "Area Or Perimeter:",font=
('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_aside = tk.Label(window,text = "A Side:",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_bside = tk.Label(window,text = "B Side:",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_cside = tk.Label(window,text = "C Side:",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
# Entry boxes for shape,aside and bside and cside
e_aside = tk.Entry(window,width=5)
e_bside = tk.Entry(window,width=5)
e_cside = tk.Entry(window,width=5)

# Combobox creation
n = tk.StringVar()
shape_chosen = ttk.Combobox(window, textvariable = n, width=14, state="readonly")


# Adding combobox drop down list

shape_chosen['values'] = ('Select a shape...', 
                          'Square', 
                          'Circle',
                          'Triangle',
                          'Parallelogram')
# Shows Select a shape as a default value
shape_chosen.current(0)

n = tk.StringVar()
form_chosen = ttk.Combobox(window, textvariable = n, width=14, state="readonly")


# Adding combobox drop down list

form_chosen['values'] = ('Area or Perimeter...', 
                          'Perimeter', 
                          'Area')
# Shows Select a shape as a default value
form_chosen.current(0)

# Button to calculate age 
btn_calculate_ap = tk.Button(window,text="Calculate area/perimeter",font=("Arial",13), command=validation)
 
# Label for text box that will display the calculated age
lb_calculated_ap = tk.Label(window,text="The calculated area/perimeter is",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
tbox_ap=tk.Text(window,width=3,height=0,state="disabled",bg="#99ade6",font=('Arial',24,"bold"))

# Button to exit application
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)



# Placing the elements on the screen
lb_heading.place(x=180,y=5)
lb_subheading.place(x=20,y=50)
lb_ap.place(x=20,y=230)
#month
lb_shape.place(x=20,y=110)
#date
lb_aside.place(x=20,y=140)
e_aside.place(x=120,y=140)
#year
lb_bside.place(x=20,y=170)
e_bside.place(x=120,y=170)
#cside
lb_cside.place (x=20, y=200)
e_cside.place (x=120, y=200)
#e_shape.place(x=120,y=105)
shape_chosen.place(x=120,y=110)
form_chosen.place(x=205,y=230)
btn_calculate_ap.place(x=30,y=350)
lb_calculated_ap.place(x=310,y=70)
tbox_ap.place(x=425,y=100)
btn_exit.place(x=500,y=350)