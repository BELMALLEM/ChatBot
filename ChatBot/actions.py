# import wikipedia for the search
import wikipedia
import requests
import random
import json
import smtplib
import conf
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

random.seed()
class actions():
    """docstring for actions."""

    def __init__(self):
        super(actions, self).__init__()

    # the function responsible of doing some researches for the user
    def search(self, phrase):
        try:
            a = wikipedia.summary(phrase, sentences=1)
            print(a.encode("utf-8"))
            return a.encode("utf-8")
        except wikipedia.exceptions.DisambiguationError as e:
            print(" {0}".format(e))

    def news(self):
        a = requests.get("https://myallies-breaking-news-v1.p.rapidapi.com/GetTopNews",
             headers={
                   "X-RapidAPI-Host": "myallies-breaking-news-v1.p.rapidapi.com",
                   "X-RapidAPI-Key": "2f9a3e54a3msh878ed42b27b4202p198f76jsn7ec2aff3beb0"
                      }
                    )
        print(random.choice(a.json()['Data'])['MainTitle'])

        # script to send an email just setup the conf.py file and the msg
        def send_mail(self, subject, msg):
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(conf.EMAIL_ADDRESS_FROM, conf.PASSWORD)
                message = 'Subject:{}\n\n{}'.format(subject, msg)
                server.sendmail(conf.EMAIL_ADDRESS_FROM, conf.EMAIL_ADDRESS_TO, message)
                server.quit()
                print("Success: Email sent!")
