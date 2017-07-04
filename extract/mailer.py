from IPython.display import display,HTML
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class sendEmail():
  def __init__(self, graph_url, graph_subject):
    self.graph_recipients = 'nehaabrol87@gmail.com,jonathan.m.barton@gmail.com'
    self.graph_sender = 'nehaabrolplotly@gmail.com'
    self.graph_url = graph_url
    self.graph_subject = graph_subject
    self.EMAIL_USERNAME = os.environ['PLOTLY_EMAIL_USERNAME']
    self.EMAIL_PASSWORD = os.environ['PLOTLY_EMAIL_PASSWORD']
    self.createTempelate()
    self.send()

  def createTempelate(self):
    global email_body
    graph_url = self.graph_url
    template = (''
      '<a href="{graph_url}" target="_blank">' # Open the interactive graph when you click on the image
          '<img src="{graph_url}.png">'        # Use the ".png" magic url so that the latest, most-up-to-date image is included
      '</a>'
      '{caption}'                              # Optional caption to include below the graph
      '<br>'                                   # Line break
      '<a href="{graph_url}" style="color: rgb(190,190,190); text-decoration: none; font-weight: 200;" target="_blank">'
          'Click to comment and see the interactive graph'  # Direct readers to Plotly for commenting, interactive graph
      '</a>'
      '<br>'
      '<hr>'                                   # horizontal line
      '')
    email_body = ''
    _ = template
    _ = _.format(graph_url=graph_url, caption='')
    email_body += _

  def send(self):
    me  = self.graph_sender
    recipient = self.graph_recipients
    email_server_host = 'smtp.gmail.com'
    port = 587
    email_username = self.EMAIL_USERNAME
    email_password = self.EMAIL_PASSWORD
    
    msg = MIMEMultipart('alternative')
    msg['From'] = me
    msg['To'] = recipient
    msg['Subject'] = self.graph_subject
    msg.attach(MIMEText(email_body, 'html'))
    server = smtplib.SMTP(email_server_host, port)
    server.ehlo()
    server.starttls()
    server.login(email_username, email_password)
    server.sendmail(me, recipient, msg.as_string())
    server.close()
    print 'Email sent for' + self.graph_subject + ' to ' + recipient