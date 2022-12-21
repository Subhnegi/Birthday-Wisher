##################### Extra Hard Starting Project ######################
from debugpy import connect
import pandas
import datetime as dt
from random import  randint
import smtplib

# 1. Update the birthdays.csv
#check for todays date
now=dt.datetime.now()
today_month=now.month
today_day=now.day
# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict=data.to_dict(orient='records')
for i in data_dict:
    if i["month"]==today_month and i["day"]==today_day:
        recipient_name=i["name"]
        recipient_mail=i["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        j=randint(1,3)
        with open(f".\letter_templates\letter_{j}.txt") as datafile:
            letter=datafile.read()
            letter=letter.replace("[NAME]",recipient_name)
# 4. Send the letter generated in step 3 to that person's email address.
        my_mail="subhnegipython@gmail.com"
        my_password="poaxujigalppestq"
        with smtplib.SMTP_SSL("smtp.gmail.com") as connect:
            connect.login(user=my_mail,password=my_password)
            connect.sendmail(from_addr=my_mail,to_addrs=recipient_mail,msg=f"Subject: Happy Birthday\n\n {letter}")



