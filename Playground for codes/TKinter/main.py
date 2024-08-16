import tkinter

window = tkinter.Tk()
window.title("My First GPU")                                                        # Setting the title of the Screen
window.minsize(width=500, height=300)                                               # Setting the window size
window.config(padx=20,pady=20)                                                      # Padding the window so that all the widgets gets more space around the window

def button_got_clicked():
    print("I am clicked")
    my_label.config(text="I am a new Label using config function")                  # Using config to change the label text
    new_text = input.get()                                                          # get the value of the input variable using Entry class
    my_label.config(text=new_text)                                                  # defining the text as my_text
    my_label.grid(column=0, row=0)

#label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))           # Defining the label
#my_label.pack(side="top")                                                          # Assigning the label to the top of the screen
my_label.grid(column=0, row=0)                                                      # Assigning the position of label with the grid function
my_label.config(padx=20,pady=20)                                                    # Adds space around the my_label that is pushes the other buttons near it by 20 spaces

# Button

button = tkinter.Button(text="Click Me",command=button_got_clicked)                 # Using button class to create a pressable button with a name and command
#button.pack()
button.grid(column=1, row=1)

# New Button

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
#input.pack()
input.grid(column=3, row=2)



# Holds the output screen
window.mainloop()