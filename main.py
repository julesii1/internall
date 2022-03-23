# ____________   IMPORTS ________________
# Getting current date from import date function from datetime module
from datetime import date
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# ____________   FUNCTIONS ________________
def find_ap(d, m, y):
    # find the age ( difference between current and date of birth )
    age = today.xside-y-((today.shape, today.day)<(m,d))
    return age
def display_calc_ap(age):
    tbox_age.config(state='normal')
    #age calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_age.delete('1.0', tk.END)
    tbox_age.insert(tk.END,age)
    tbox_age.config(state='disabled')
def validation():
  # gets the three entries
  d = e_yrside.get()
  m = shape_chosen.current()
  #m = e_shape.get()
  y = e_xside.get()
  msg = ''
  if len(d) == 0 or len (y) == 0:
      msg = 'day, shape and xside can\'t be empty'
  else:
    try:
      if any(ch.isdigit() for ch in d) == False:
        msg = 'day must be a NUMBER'
      elif m == 0:
        msg = 'choose an appropriate SHAPE'
      elif any(ch.isdigit() for ch in y) == False:
        msg = 'xside must be a NUMBER'
      else:
       # msg = 'Success!'
        day = int(d)
        shape = m #shape is already in number from list position
        xside = int(y)
        calc_age = find_ap(day, shape, xside)
        display_calc_ap(calc_age)
            
    except Exception as ep:
      messagebox.showerror('error', ep)
      
  if msg != '':
    messagebox.showinfo('message', msg)
def exit():
    window.destroy()
# ____________   MAIN  ________________
# Create a object which stores today’s whole yrisde using datetime function
today = date.today()
# Creating a custom window
window = tk.Tk()
window.geometry("700x400")
window.config(bg="#c7d6f5")
window.resizable(width=False,height=False)
window.title('Area Perimeter Calculator')




# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="Area Perimeter Calculator",font=("Arial", 20),fg="black",bg="#c7d6f5")
lb_subheading = tk.Label(window,font=("Arial",12),text="Input shape and numbers",fg="black",bg="#c7d6f5")
 
# Labels for yrside, shape and xside
lb_shape = tk.Label(window,text = "Shape: ",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_ap = tk.Label(window,text = "Area Or Perimeter ",font=
('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_yrside = tk.Label(window,text = "y/(r) Side:",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_xside = tk.Label(window,text = "x Side:",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
# Entry boxes for yrside, shape and xside
e_yrside = tk.Entry(window,width=5)

# Combobox creation
n = tk.StringVar()
shape_chosen = ttk.Combobox(window, textvariable = n, width=14)


# Adding combobox drop down list

shape_chosen['values'] = ('Select a shape...', 
                          'Square', 
                          'Circle',
                          'Triangle',
                          'Parallelogram')
# Shows Select a shape as a default value
shape_chosen.current(0)

n = tk.StringVar()
form_chosen = ttk.Combobox(window, textvariable = n, width=14)


# Adding combobox drop down list

form_chosen['values'] = ('Area or Perimeter...', 
                          'Perimeter', 
                          'Area')
# Shows Select a shape as a default value
form_chosen.current(0)

#e_shape = tk.Entry(window,width=5)
e_xside = tk.Entry(window,width=5)
# Button to calculate age 
btn_calculate_age = tk.Button(window,text="Calculate area/perimeter",font=("Arial",13), command=validation)
 
# Label for text box that will display the calculated age
lb_calculated_age = tk.Label(window,text="The calculated area/perimeter is",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
tbox_age=tk.Text(window,width=3,height=0,state="disabled",bg="#99ade6",font=('Arial',24,"bold"))

# Button to exit application
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)



# Placing the elements on the screen
lb_heading.place(x=180,y=5)
lb_subheading.place(x=20,y=50)
lb_ap.place(x=20,y=200)
lb_shape.place(x=20,y=110)
lb_yrside.place(x=20,y=140)
lb_xside.place(x=20,y=170)
e_yrside.place(x=120,y=140)
#e_shape.place(x=120,y=105)
shape_chosen.place(x=120,y=110)
form_chosen.place(x=35,y=225)
e_xside.place(x=120,y=170)
btn_calculate_age.place(x=30,y=300)
lb_calculated_age.place(x=310,y=70)
tbox_age.place(x=425,y=100)
btn_exit.place(x=500,y=350)