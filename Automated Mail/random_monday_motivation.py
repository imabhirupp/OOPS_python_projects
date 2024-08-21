import smtplib
import datetime as dt
import random

random_quote = ""


def quotes():
    global random_quote
    with open(file="quotes.txt") as quote:
        all_quotes = quote.readlines()
        random_quote = random.choice(all_quotes)


def send_mail():
    quotes()
    global random_quote
    email = "abhiruptest12@gmail.com"
    password = "qlwfxybawtngihoh"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="abhirupsinha@yahoo.com", msg=f"Subject: Monday Motivation\n\n {random_quote}")
    connection.close()


current_day = dt.datetime.now()
day = current_day.weekday()

if day == 1:
    send_mail()
else:
    print("Not applicable")
