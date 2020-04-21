import smtplib
from email.mime.text import MIMEText
from ...settings import *


class SendMail:
    """
    This class is for starting smtp and send email to other accounts.
    """

    def __init__(self):
        self.connnection = self.connect()  # initialize connect

    def connect(self):
        """ this method is used to connect the mail service"""
        try:
            s = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            s.starttls()
            s.login(EMAIL_HOST_USERNAME, EMAIL_HOST_PASSWORD)
            print("================> email service is started: {}".format(s))
            return s
        except:
            return "email service is failed"

    def send_mail(self, email, data):
        print(email)
        msg = MIMEText(data)
        print(msg)
        self.connnection.sendmail(EMAIL_HOST_USERNAME, email, msg.as_string())
        self.connnection.quit()
