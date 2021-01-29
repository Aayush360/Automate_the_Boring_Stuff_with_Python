## pip install imapclient
## pip install  pip install pyzmail36

import imapclient
import pyzmail
from datetime import datetime as date

# create connection obj and pass domain name along with ssl encryption

conn = imapclient.IMAPClient('imap.gmail.com',ssl=True)

# login to email -- returns byte object which tells if authentication is success

conn.login('paudelaayus@gmail.com','uirkzesmlbnhcvup')

# lets select a folder (INBOX most of the time, readonly=True unless you are going to delete email)
# can check spam , outbox, draft etc
conn.select_folder('INBOX',readonly=True)

## to list the available folders
print('list of folders: \n-----------------',conn.list_folders())

# find the email
# search using the from email-add -- returns unique id each of which refers to the email in the mailbox as a list
uids=conn.search(['FROM','paudelaayus@gmail.com'])
# print(uids)
# email and part you want to extract
raw_message = conn.fetch([8099],['BODY[]','FLAGS'])

# use pyzmail to parse the raw_email,, provide 2 keys, first is the main key of the dictionary object,, second is key within the key
message = pyzmail.PyzMessage.factory(raw_message[8099][b'BODY[]'])

# to get the subject
subject = message.get_subject()
print('subject is: ',subject)
# to get the address -- returns sender name and email
from_add = message.get_addresses('from')
print('from_address',from_add)

to_add = message.get_addresses('to')
print('to_address: ',to_add)

bcc = message.get_addresses('bcc')
print('bcc: ',bcc)

# to check if it is text or html or both
is_text = message.text_part
print('return if it is text: ',is_text)
is_html = message.html_part
print('return if it is html: ',is_html)

# to get the message payload(actual data)
pay_load=message.text_part.get_payload().decode('utf-8')
print('pay_load: ', pay_load)


## to delete the folder, pass readonly as False
conn.select_folder('INBOX',readonly=False)
uids = conn.search([u'SINCE', date(2021,1,29)])
print('ids: ',uids)

# to delete the mail send uids as list

conn.delete_messages([8099])

## finally
conn.logout()