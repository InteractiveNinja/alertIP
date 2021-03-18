import smtplib
from smtplib import SMTPException
class mailSender:
    def __init__(self,configsvals):
        self.mail : str = configsvals["alertmail"]
        self.sender : str = configsvals["sender"]
        self.smtp : str = configsvals["smtp"]
        self.port : str = configsvals["port"]
        self.senderpass : str = configsvals["senderpass"]
    
    def sendMail(self):

        message = """
        Die Public Adress hat sich geaendert, bitte kontrollieren und das Warnscript umconfigurieren.
        """
        server = smtplib.SMTP(self.smtp,self.port)
        server.starttls()
        server.login(self.sender,self.senderpass)
        try:
            server.sendmail(self.sender,self.mail,message)
        except SMTPException as e:
            print("Fehler beim erstellen der Mail")
            print(e)