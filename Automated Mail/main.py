import smtplib

my_email = "abhiruptest12@gmail.com"
password = "qlwfxybawtngihoh"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="abhirupsinha@yahoo.com", msg="hello")
connection.close()




