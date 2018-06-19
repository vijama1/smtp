import imaplib
import base64
import getpass
import requests
from bs4 import BeautifulSoup
import time
#email_user = input('Email: ')
email_pass = getpass.getpass()

M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
M.login('amanvijay97@gmail.com', email_pass)
M.select('inbox')
list=[]
#typ, data = M.search(None, 'ALL')
typ, message_numbers = M.search(None, 'ALL')
# print(message_numbers[0].split())
# print(message_numbers[0].split().rever)
for num in message_numbers[0].split()[::-1]:
    typ, data = M.fetch(num, '(RFC822)')
    data1 = data[0][1].decode()
    data_new=str(data1)
    cleantext = BeautifulSoup(data1, "html5lib")
    #final_data=cleantext.get_text()
    good_data=cleantext.get_text(strip=True)
    #print(good_data)
    to=good_data.index("To")
    #print(to)
    nw=good_data.index("Received")
    #print(nw)
    receiver_mail=good_data[to+4:nw]
    print("Receiver mail: "+str(receiver_mail))
    date_index=good_data.index("Date: ")
    sublist=good_data[date_index:]
    new=sublist.index("//n")
    print(new)
    time.sleep(5)
    print(sublist)

    try:
        sub1=sublist.index("Subject")
        sub2=sublist.index("Message-ID")
        subject=sublist[sub1:sub2]
        print("Subject: "+str(subject))
    except:
        print("No subject")

    print("===================================")
    if input()=="n":
        pass
M.close()
M.logout()
