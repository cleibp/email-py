import imaplib
import email

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login("seuemail@gmail.com", "suasenha")
imap.select("inbox")

status, emails = imap.search(None, "(UNSEEN)")

email_dict = {}

for email_id in emails[0].split():
	status, email_data = imap.fetch(email_id, "(RFC822)")
	email_message = email.message_from_bytes(email_data[0][1])
	subject = email_message["Subject"]
	body = email_message.get_payload()[0].get_payload()
	email_dict[subject] = body

imap.close()
imap.logout()
print(email_dict)
