import csv
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

def main():
     with open('CSVINPROJECT.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['User.Voice.ExternalVoiceMailGreeting'] == '':
                #print('User '+row['User.Email']+ ', ' +row['User.Voice.Extension']+ ', does not have a External VM')
                unconfigured_emails = row['User.Email']
                for i in enumerate(unconfigured_emails[1]):
                    print (unconfigured_emails)
                    email_them(unconfigured_emails)

def email_them(unconfigured_emails):
    From  = 'no-reply@'
    To = unconfigured_emails
    with open('message.txt') as fp:
        msg = MIMEText(fp.read())
    msg['Subject'] = ''
    msg['From'] = From
    msg['To'] = To
    s = smtplib.SMTP('')
    s.sendmail(From, [To], msg.as_string())
    s.quit()

main()