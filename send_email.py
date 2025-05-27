import smtplib, ssl
import os
from dotenv import load_dotenv



def send_email(user_msg):

    load_dotenv()

    # print(os.getenv("EMAIL_HOST"))
    # print(os.getenv("PORT"))
    # print(os.getenv("USRNAME"))
    # print(os.getenv("PASSWORD"))
    # print(os.getenv("RECEIVER"))
    
    host = os.getenv("EMAIL_HOST")
    port = os.getenv("PORT")


    username = os.getenv("USRNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("RECEIVER")

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_msg)