from tkinter import *                # Imports all the classes of tkinter
from tkinter import messagebox       # We have to import it because it's not a class and is a code
import random
import pyperclip                     # Used in copy pasting in python
import json
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
    new_data = {
        website_detail: {                                                                  # Creating a dictionary with the website value entered by the user and the email and passwords along with it
            "Email/Username": username_detail,
            "Password": password_detail,
        }
    }
    # Checking if the user forgot to enter any detail
    if len(website_detail) == 0 or len(username_detail) == 0 or len(password_detail) == 0:
        messagebox.showinfo(title="Oops", message="Incomplete Details")
    else:
        try:
            # Saving the details entered by the user in a new text file
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:                                                         # If file not found, creating a new file with that name
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)                                  # Adding the data inside the file using json.dump
        else:
            # Updating old data with new_data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)                                      # Data file is the location to dump this data and new_data is the data we want to add
        finally:
            website_value.delete(0, END)
            username_value.delete(0, END)
            password_value.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    
    website_detail = website_value.get()
    try:                                                                                  # Trying to read the data.json file
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:                                                             # If the file is not found then show error message
        messagebox.showinfo(title="Error", message="File does not exist")
    else:                                                                                 # If found then return the details associated with it
        if website_detail in data:
            username = data[website_detail]["Email/Username"]
            password = data[website_detail]["Password"]
            messagebox.showinfo(title=website_detail, 
                                message=f"Email: {username}\nPassword: {password}")
        else:                                                                             # If the file is found but the website name entered doesn't exist then show error message                                                                                
            messagebox.showinfo(title="Error", message=f"No details for the "
                                                       f"{website_detail} you are searching for.")
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

search = Button(text="Search", width=13, command=find_password)
search.grid(column=3, row=1)


window.mainloop()
