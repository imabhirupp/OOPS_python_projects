import random
import smtplib
import pandas
import datetime as dt

my_email = "abhiruptest12@gmail.com"
password = "qlwfxybawtngihoh"

current = dt.datetime.now()
current_tuple = (current.month, current.day)                                                                            # Saving the current day and month in a tuple
# day = current.day
# month = current.month

data = pandas.read_csv("birthdays.csv")                                                                                 # Accessing the contents of the birthday file
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}               # Creating a dict with month and day using iterrows

if current_tuple in birthday_dict:                                                                                      # Checking if the current day and month of tuple in the dict
    birthday_person = birthday_dict[current_tuple]                                                                      # 
    file = f"letter_templates/letter_{random.randint(1,3)}.txt"                                                   # Selecting random letter format from the saved formats

    with open(file) as letter_file:                                                                                     # Opening the letter
        content = letter_file.read()                                                                                    # Reading the contents
        content = content.replace("[NAME]", birthday_person["name"])                                              # Replacing the [NAME] with the name of the birthday person


with smtplib.SMTP("smtp.gmail.com") as connections:                                                                     # Establishing connection
    connections.starttls()
    connections.login(user=my_email, password=password)                                                                 # Logging into the mail
    connections.sendmail(from_addr=my_email,                                                                            # Sending the mail
                         to_addrs=birthday_person["email"],
                         msg=f"Subject:Happy Birthday:\n\n{content}")




