import tkinter

window = tkinter.Tk()
window.title("Km to Miles Converter")                               # Setting the title of the Screen
window.minsize(width=250, height=250)                               # Setting the window size
window.config(padx=20,pady=20)                                      # Padding the window so that all the widgets gets more space around the window

# When the button is pressed
def button_clicked():
    converter()

# Converting miles into km
def converter():
    values = float(value.get())
    km = round(values * 1.609344)
    km_result.config(text=km)
    km_result.grid(column=1,row=1)

# Defining the miles_text in the window

miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=2, row=0)
miles_text.config(padx=10, pady=10)

# Defining the equal_text in the window

equal_text = tkinter.Label(text="is equal to")
equal_text.grid(column=0,row=1)
equal_text.config(padx=10,pady=10)

# Defining the km_text in the window

km_text = tkinter.Label(text="km")
km_text.grid(column=2,row=1)
km_text.config(padx=10,pady=10)

# # Defining the km_result in the window

km_result = tkinter.Label(text="0")
km_result.grid(column=1,row=1)

# # Defining the calculate button in the window

calculate = tkinter.Button(text="Calculate", command=button_clicked)
calculate.grid(column=1,row=2)

# Entry i.e. taking input of the value to convert

value = tkinter.Entry(width=20)
value.grid(column=1, row=0)


window.mainloop()