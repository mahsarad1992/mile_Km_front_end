# import all classes of "tkinter" module
from tkinter import *

# creat first object, a window to work on, using "Tk()" class
window = Tk()
window.title("mile-kilometer-Convertor")
window.wm_minsize(width=400, height=200)
# consider a margin around the window
window.config(padx=50, pady=50)

# creat 3 lables: "mile", "kilometer", and "is equal to" and place them on the desired locations on the window
lable1 = Label(text="is equal to:")
lable1.grid(column=0, row=2)
lable1.config(padx=10, pady=10)

lable2 = Label(text="Mile")
lable2.grid(column=2, row=0)
lable2.config(padx=10, pady=10)

lable3 = Label(text="Kilometer")
lable3.grid(column=2, row=2)
lable3.config(padx=10, pady=10)

# creat an "entry" tab for user to insert a number (as "mile" that they wish to convert to Km)
entry = Entry(width=8)
# place the "entry" tab in an appropriate location
entry.grid(column=1, row=0)

# define the calculator function
def calculator():
    """
    This function gets the number that the user typed on the entry tab,
    formats it to a float
    and after calculation, represents it as a lable placed in an appropriate location
    """
    number = float(entry.get())
    km = format(number / 0.62137, '.4f')
    new_number = Label(text=f"{km}")
    new_number.grid(column=1, row=2)

# creat a button that the user could click on to trigger the calculation
button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=3)

# the window stays open unless the user close it
window.mainloop()
