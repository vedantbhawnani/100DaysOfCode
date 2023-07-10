import smtplib
import datetime as dt
import random

mail = "@gmail.com"
password = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\day32\\quotes.txt") as quote:
        quotes = quote.readlines()
        today_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mail, password=password)
        connection.sendmail(
            from_addr=mail, 
            to_addrs="siddhishettyspam@gmail.com", 
            msg=f"Subject: Motivation \n\n {today_quote}"
        )