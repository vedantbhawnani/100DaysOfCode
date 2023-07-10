import pandas as pd
import smtplib 
import datetime as dt

MAIL = "testcheck366@gmail.com"
PASSWORD = "qozkqbosdlrydoue"

dates = pd.read_csv("C:\\Users\\vedan\\codes\\100DaysOfCode\\day32\\birthdates.csv")
now = dt.datetime.now()

for index,row in dates.iterrows():

    if now.month == row.month and now.day == row.day:
        with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\day32\\letter.txt","r") as letter:
            data = letter.read()
            data = data.replace("[NAME]", row.names)
            
            
        with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\day32\\letter.txt","w") as letter:
            letter.write(data)
        with open("C:\\Users\\vedan\\codes\\100DaysOfCode\\day32\\letter.txt","r") as letter:
            wish = letter.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MAIL,
                to_addrs=MAIL,
                msg = f"Subject: Cheers\n\n{wish}"
            )

