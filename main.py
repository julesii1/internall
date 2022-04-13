# ____________   IMPORTS ________________
# Getting current date from import date function from datetime module

# used to create a custom window for a/p calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functions import *
import tkinter.simpledialog as sd

#from PIL import ImageTk, Image

# ____________   FUNCTIONS ________________
def find_ap():

    while True:
        try:
            # gets two entries
            s = shape_chosen.current()
            a_p = form_chosen.current()

            # all formulas for area
            if s == 1:
                #print("Square")

                #pop('aos.py')
                if a_p == 1:  #perimeter
                    #print("Perimeter of a Square")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    length = sd.askfloat('User Input',
                                         'Enter the WIDTH of square:',
                                         **options)
                    height = sd.askfloat('User Input',
                                         'Enter the HEIGHT of square:',
                                         **options)
                    display_calc_ap(get_rec_square_perimeter(length, height))
                    #enter height
                    #enter width
                else:
                    #area
                    #print("Area of Square")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    length = sd.askfloat('User Input',
                                         'Enter the WIDTH of square:',
                                         **options)
                    height = sd.askfloat('User Input',
                                         'Enter the HEIGHT of square:',
                                         **options)
                    display_calc_ap(get_rec_square_area(length, height))
                break
            elif s == 2:
                #print("Circle")
                #pop('aoc.py')
                if a_p == 1:  #perimeter
                    #print("Perimeter of Circle")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    userInput = sd.askfloat('User Input',
                                            'Enter the Radius of circle:',
                                            **options)
                    display_calc_ap(get_circle_perimeter(userInput))
                elif a_p == 2:

                    #area
                    #https://stackoverflow.com/questions/51394482/is-it-possible-to-display-python-input-statements-in-tkinter
                    #print("Area of Circle")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    userInput = sd.askfloat('User Input',
                                            'Enter the Radius of circle:',
                                            **options)
                    display_calc_ap(get_circle_area(userInput))
                    #r=sd.askstring("Enter the Radius of circle: ")
                    #circle_area(r)
                else:
                    print("Option not available")
                break

            elif s == 3:  #watch indentation Jules - working my side now!
                #print("Triangle")
                if a_p == 1:

                    #print("Perimeter of triangle")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    length1 = sd.askfloat(
                        'User Input', 'Enter the Bottom value of triangle:',
                        **options)
                    length2 = sd.askfloat(
                        'User Input', 'Enter the Side 2 value of triangle:',
                        **options)
                    height = sd.askfloat('User Input',
                                         'Enter the Side value of triangle:',
                                         **options)
                    display_calc_ap(get_triangle_perimeter(length1, length2, height))

                else:

                    #print("Area of Triangle")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    base = sd.askfloat('User Input',
                                       'Enter the WIDTH of triangle:',
                                       **options)
                    height = sd.askfloat('User Input',
                                         'Enter the HEIGHT of triangle:',
                                         **options)
                    display_calc_ap(get_triangle_area(base, height))
                break
            elif s == 4:  
                #print("Parallelogram")
                if a_p == 2:

                    #print("Perimeter of Parallelogram")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    length = sd.askfloat(
                        'User Input', 'Enter the LENGTH of parallelogram:',
                        **options)
                    height = sd.askfloat('User Input',
                                         'Enter the HEIGHT of parallelogram:',
                                         **options)
                    display_calc_ap(get_rec_parallelogram_perimeter(length, height))

                if a_p == 1:

                    #print("Area of Parallelogram")
                    options = {'minvalue': 3.0, 'maxvalue': 10.0}
                    base = sd.askfloat('User Input',
                                       'Enter the LENGTH of parallelogram:',
                                       **options)
                    height = sd.askfloat('User Input',
                                         'Enter the HEIGHT of parallelogram:',
                                         **options)
                    display_calc_ap(get_rec_parallelogram_area(base, height))
                break

        #pop('aot.py')

        except ValueError:
            print("You have inputted a incorrect value")
            break

        except TypeError: 
            print("You have tried to exit without input")

def display_calc_ap(ap):
    tbox_ap.config(state='normal')
    #a/p calculated is inserted into the text box after clearing the previous info in the textbox.
    tbox_ap.delete('1.0', tk.END)
    tbox_ap.insert(tk.END, ap)
    tbox_ap.config(state='disabled')


def exit():
    window.destroy()


# ____________   MAIN  ________________
# Create a object which stores today’s whole yrisde using datetime function

# Creating a custom window
window = tk.Tk()
window.geometry("700x400")
window.config(bg="#c7d6f5")
window.resizable(width=False, height=False)
window.title('Area Perimeter Calculator')

# Labels for Heading and Subheadng of GUI
lb_heading = tk.Label(window,
                      text="Area Perimeter Calculator",
                      font=("Arial", 20),
                      fg="black",
                      bg="#c7d6f5")
lb_subheading = tk.Label(window,
                         font=("Arial", 12),
                         text="Input shape and numbers",
                         fg="black",
                         bg="#c7d6f5")

# Labels for shape, ap
lb_shape = tk.Label(window,
                    text="Shape: ",
                    font=('Arial', 12, "bold"),
                    fg="#000000",
                    bg="#c7d6f5")
lb_ap = tk.Label(window,
                 text="Area Or Perimeter:",
                 font=('Arial', 12, "bold"),
                 fg="#000000",
                 bg="#c7d6f5")

# Combobox creation
n = tk.StringVar()
shape_chosen = ttk.Combobox(window, textvariable=n, width=18, state="readonly")

# Adding combobox drop down list

shape_chosen['values'] = ('Select a shape...', 'Square/Tapawha', 'Circle/Porowhita', 'Triangle/Tapatoru',
                          'Parallelogram/Whakarara')
# Shows Select a shape as a default value
shape_chosen.current(0)

n = tk.StringVar()
form_chosen = ttk.Combobox(window, textvariable=n, width=14, state="readonly")

# Adding combobox drop down list

form_chosen['values'] = ('Area or Perimeter...', 'Perimeter/Paenga', 'Area/Rohe')
# Shows Select a shape as a default value
form_chosen.current(0)

# Create an object of tkinter ImageTk
#img = ImageTk.PhotoImage(Image.open("nathan.png"))

# Create a Label Widget to display the text or Image
#label = Label(window, image = img)
#label.pack()

# Button to calculate age
btn_calculate_ap = tk.Button(window,
                             text="Calculate area/perimeter",
                             font=("Arial", 13),
                             command=find_ap)

# Label for text box that will display the calculated age
lb_calculated_ap = tk.Label(window,
                            text="The calculated area/perimeter is",
                            font=('Arial', 12, "bold"),
                            fg="#000000",
                            bg="#c7d6f5")

tbox_ap = tk.Text(window,
                  width=5,
                  height=0,
                  state="disabled",
                  bg="#99ade6",
                  font=('Arial', 24, "bold"))

# Button to exit application
btn_exit = tk.Button(window,
                     text="Exit Application!",
                     font=("Arial", 13),
                     command=exit)

# Placing the elements on the screen
lb_heading.place(x=180, y=5)
lb_subheading.place(x=20, y=50)
lb_ap.place(x=20, y=150)
#month
lb_shape.place(x=20, y=110)
#e_shape.place(x=120,y=105)
shape_chosen.place(x=120, y=110)
form_chosen.place(x=205, y=150)
btn_calculate_ap.place(x=30, y=200)
lb_calculated_ap.place(x=330, y=70)
tbox_ap.place(x=425, y=100)
btn_exit.place(x=400, y=200)
