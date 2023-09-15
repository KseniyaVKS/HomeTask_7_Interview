import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Mail:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"

    def send_message(self, recipients: list, message: str, subject=None):
        # send message
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

    def recieve_message(self, header=None):
        # recieve message
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':

    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None

    m = Mail(login, password)
    m.send_message(recipients, message, subject)
    m.recieve_message(header)
