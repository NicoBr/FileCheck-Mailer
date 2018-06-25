#! python3.6
import hashlib, time, smtplib
from argparse import ArgumentParser


parser = ArgumentParser(description='This programm checks a file for any modification and sends an email')
parser.add_argument("-f", "--file", dest="File",
                    help="file that is to survey",
                    required=True)
parser.add_argument("-s", "--sleep", dest="Sleeptime",
                    help="Time to wait between testing in seconds",
                    default=25)
parser.add_argument("--to", dest="Receiver",
                    help="email of the receiver",
                    required=True)
parser.add_argument("--from", dest="Sender",
                    help="email of the sender",
                    required=True)
parser.add_argument("--smtp", dest="SMTPserver",
                    help="name of the SMTP Server",
                    required=True)
parser.add_argument( "--port", dest="SMTPport",
                    help="The SMTP port",
                    default=25)
args = parser.parse_args()

message = """From: Nico Developer <{Sender}>
To: {Receivers}
Subject: Notification: file changed

This is a notification e-mail message from a Python script.
To inform you that the following file changed: {File}
""".format(Sender=args.Sender, Receivers=args.Receiver, File=args.File)

#End of variable declarations

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

while True:     #Endless repeat
    oldChecksum=md5Checksum(args.File)
    time.sleep(int(args.Sleeptime))
    print('The old checksum of ',args.File,' is', oldChecksum)
    print('The MD5 checksum of ',args.File,' is', md5Checksum(args.File))
    if oldChecksum != md5Checksum(args.File):
        print ('Ups, you changed something!')
        try:
           smtpObj = smtplib.SMTP(args.SMTPserver, int(args.SMTPport))
           smtpObj.sendmail(args.Sender, args.Receiver, message)         
           print ("Successfully sent email")
        except SMTPException:
           print ("Error: unable to send email")
