import smtplib
# make connection object using domain name and port number
conn = smtplib.SMTP('smtp.gmail.com',587)
# to start the connection
conn.ehlo()
# start tlsconnection ,, to encrypt password while sending username and password
conn.starttls()
# login
conn.login('paudelaayus@gmail.com','')
# send the mail (we can send multiple emails using sendmail function)
conn.sendmail('paudelaayus@gmail.com','paudelaayus@gmail.com','Subject: so long... \n\n Dear myself.. \n\n-Aayush')
# disconnects from SMTP server
conn.quit()

