import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.parser import Parser
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import constants as c
class MailSender:
    def __init__(s, *args, **k): #You MUST pass username,pwd,destinatary and type
        s.server = smtplib.SMTP(c.gmailServer,587)
        s.server.ehlo()
        s.server.starttls()
        s.server.login(k['username'],k['pwd'])
        s.message = MIMEMultipart()
        s.message['Subject'] = "Registros Preparatoria" if k['type'] is 3 else "Registros Profesional"
        s.message['From']= k['username']
        s.destinatary = k['destinatary']#','.join(k['destinatary'])
    def attachCSV(s, csvFile):
        report = open(csvFile,'r')
        s.message.attach(MIMEApplication(report.read(),Content_Disposition="attachment; filename='%s'"%basename(csvFile),Name=basename(csvFile)))
    def sendMail(s):
        s.server.sendmail(s.message['From'],s.destinatary, s.message.as_string())
    def __del__(s):
        s.server.quit()
