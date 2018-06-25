# FileCheck-Mailer
a script that checks the hash of a file and send an email when the hash change  

usage: filecheckmailer.py [-h] -f FILE [-s SLEEPTIME] --to RECEIVER --from  
                          SENDER --smtp SMTPSERVER [--port SMTPPORT]  

This programm checks a file for any modification and sends an email  
  
optional arguments:  
  -h, --help            show this help message and exit  
  -f FILE, --file FILE  file that is to survey  
  -s SLEEPTIME, --sleep SLEEPTIME  
                        Time to wait between testing in seconds  
  --to RECEIVER         email of the receiver  
  --from SENDER         email of the sender  
  --smtp SMTPSERVER     name of the SMTP Server  
  --port SMTPPORT       The SMTP port  
  
