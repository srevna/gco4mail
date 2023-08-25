from email.message import EmailMessage
import smtplib

sender = "bailey.laura8743@yahoo.com"
recipient = "gabin@sillap.fr"
password = "hhpveggttphhoskn"
message = "Hey bro how arz all good??x )"

email = EmailMessage()
email["From"] = sender
email["To"] = recipient
email["Subject"] = "hEY BROOther"
email.set_content(message)

smtp = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
smtp.starttls()
smtp.login(sender, password)
smtp.sendmail(sender, recipient, email.as_string())
smtp.quit()


# from email.message import EmailMessage
# import smtplib

