import os
import pandas as pd
import random
import datetime as dt
import smtplib


my_email = os.environ.get("my_email")
password = os.environ.get("password")

today = dt.datetime.now()
_month = today.month
_day = today.day

data = pd.read_csv("birthdays.csv")

birthday = data[(data["day"] == _day) & (data["month"] == _month)]
birthday_list = birthday.values.tolist()

if len(birthday_list) > 0:
    for person in birthday_list:
        letter = random.randint(1,3)
        with open(f"letter_templates/letter_{letter}.txt") as file:
            contend = file.read()
        letter_with_name = contend.replace("[NAME]", person[0])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # make connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person[1],
                msg=f"Subject:Happy Birthday!!!\n\n{letter_with_name}"
            )
