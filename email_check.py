import smtplib
import re
import socket
import dns.resolver
email_address=input("Enter the email address:")
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address)
records=""
if match == None:
    print('Bad Syntax in ' + addressToVerify)
    raise ValueError('Bad Syntax')
domain_name = email_address.split('@')[1]
try:
    records = dns.resolver.query(domain_name, 'MX')
    #print(records)
except:
    print("Invalid domain")
str_domain_name=str(records)
if 'object' in str_domain_name.split():
    print("Valid domain")
#print(records)
#print(records[0])
mxRecord = records[0].exchange
#print(mxRecord)
mxRecord = str(mxRecord)
# # print(mxRecord)
#print("=========")
host = socket.gethostname()
#print(host)
server = smtplib.SMTP()
server.connect(mxRecord)
server.helo(host)
server.mail('sample@qwerty.com')
code, message = server.rcpt(str(email_address))
server.quit()
# print(code)
# print(message)
# #
# # # Assume 250 as Success
if code == 250:
    print('Valid email address')
else:
    print('Invalid email address')
