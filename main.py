# ____________   IMPORTS ________________
# Getting current date from import date function from datetime module

# used to create a custom window for a/p calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



#from PIL import ImageTk, Image

# ____________   FUNCTIONS ________________

def pop():
  window.destroy()
  exec(open('aot.py').read())
  
def find_ap (shape):

    # gets the five entries
  s = shape_chosen.current()
  f = form_chosen.current()
  
  # all formulas for area
  if s == 'Circle':
    print(
      "circle"
    )
      
    
def display_calc_ap(ap):
    tbox_ap.config(state='normal')
    #a/p calculated is inserted into the text box after clearing the previous info in the textbox. 
    tbox_ap.delete('1.0', tk.END)
    tbox_ap.insert(tk.END,ap)
    tbox_ap.config(state='disabled')
def validation():
  # gets the five entries
  s = shape_chosen.current()
  f = form_chosen.current()

  if f == 'Area':
   print("Area Chosen")
  elif f == 'Perimeter':
    print("Perimeter Chosen")      
  calc_ap = find_ap("shape")
  display_calc_ap(calc_ap)
          
      
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

root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="ball.ppm")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop() 

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,text="Area Perimeter Calculator",font=("Arial", 20),fg="black",bg="#c7d6f5")
lb_subheading = tk.Label(window,font=("Arial",12),text="Input shape and numbers",fg="black",bg="#c7d6f5")
 
# Labels for shape, ap
lb_shape = tk.Label(window,text = "Shape: ",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
lb_ap = tk.Label(window,text = "Area Or Perimeter:",font=
('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")

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

# Create an object of tkinter ImageTk
#img = ImageTk.PhotoImage(Image.open("nathan.png"))

# Create a Label Widget to display the text or Image
#label = Label(window, image = img)
#label.pack()


# Button to calculate age 
btn_calculate_ap = tk.Button(window,text="Calculate area/perimeter",font=("Arial",13), command=pop)
 
# Label for text box that will display the calculated age
lb_calculated_ap = tk.Label(window,text="The calculated area/perimeter is",font=('Arial',12,"bold"),fg="#000000",bg="#c7d6f5")
tbox_ap=tk.Text(window,width=3,height=0,state="disabled",bg="#99ade6",font=('Arial',24,"bold"))

# Button to exit application
btn_exit = tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)



# Placing the elements on the screen
lb_heading.place(x=180,y=5)
lb_subheading.place(x=20,y=50)
lb_ap.place(x=20,y=150)
#month
lb_shape.place(x=20,y=110)
#e_shape.place(x=120,y=105)
shape_chosen.place(x=120,y=110)
form_chosen.place(x=205,y=150)
btn_calculate_ap.place(x=30,y=350)
lb_calculated_ap.place(x=310,y=70)
tbox_ap.place(x=425,y=100)
btn_exit.place(x=500,y=350)
