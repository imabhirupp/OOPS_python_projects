from tkinter import *                # Imports all the classes of tkinter
from tkinter import messagebox       # We have to import it because it's not a class and is a code
import random
import pyperclip                     # Used in copy pasting in python

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]                  # Using python comprehension to reduce the code
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers                  # Concatinating all the items in password to form the random password

    random.shuffle(password_list)

    passwords = "".join(password_list)
    password_value.insert(0, passwords)
    pyperclip.copy(passwords)                                                               # Using pyperclip to copy the randomly generated password and saving it in the clipboard for use

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Getting the values from the Entries
    website_detail = website_value.get()
    username_detail = username_value.get()
    password_detail = password_value.get()

    # Checking if the user forgot to enter any detail
    if len(website_detail) == 0 or len(username_detail) == 0 or len(password_detail) == 0:
        messagebox.showinfo(title="Oops", message="Incomplete Details")
    else:
        is_yes = messagebox.askyesno(title=website_detail, message="Are you sure, "
                                                                   "you want to save these details?")
        # Saving the details entered by the user in a new text file
        if is_yes:
            with open("details.txt", "a") as data_file:
                data_file.write(f"{website_detail} | {username_detail} | {password_detail}\n")
                website_value.delete(0, END)
                username_value.delete(0, END)
                password_value.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Loading the image of the window
logo_image = PhotoImage(file="logo.png")

# CANVAS

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# LABEL

website = Label(text="Website:")
website.grid(column=0,row=1)

username = Label(text="Email/Username:")
username.grid(column=0,row=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

# ENTRY

website_value = Entry(width=50)
website_value.grid(column=1, row=1, columnspan=2)
website_value.focus()                                                  # To focus the cursor to website entry directly

username_value = Entry(width=50)
username_value.grid(column=1, row=2, columnspan=2)
username_value.insert(0, "abhirupsinha12@gmail.com")

password_value = Entry(width=32)
password_value.grid(column=1, row=3, columnspan=1)

# BUTTONS

generate = Button(text="Generate Password", command=random_password)
generate.grid(column=2, row=3)

add = Button(text="Add", width=43, command=save)
add.grid(column=1, row=4, columnspan=2)




window.mainloop()