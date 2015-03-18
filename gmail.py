#! /usr/bin/env python3

def send_email(FROM, TO, SUBJECT, TEXT):

  import smtplib
  gmail_user = 'me@gmail.com'
  gmail_pwd  = 'password'

  message    = 'From: {0}\nTo: {1}\nSubject: {2}\n\n{3}'.format(
                 FROM,
                 ', '.join(TO),
                 SUBJECT,
                 TEXT
  )

  try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
  except:
    raise Exception('failed to send mail')


FROM    = 'me@gmail.com'
TO      = [
           'you@gmail.com',
           'foo@gmail.com',
           'bar@gmail.com'
          ] #must be a list
SUBJECT = "Testing sending using gmail From Python"
TEXT    = "Testing sending mail using gmail servers"

send_email(FROM, TO, SUBJECT, TEXT)
