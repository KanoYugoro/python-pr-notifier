from email.header    import Header
from email.mime.text import MIMEText
from smtplib         import SMTP_SSL

def sendEmail(recipient,username,password,smtp_host,smtp_port,subject,body,SMTP_SSL_FUNCTION = SMTP_SSL):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = username
    msg['To'] = recipient

    # send it via gmail
    s = SMTP_SSL_FUNCTION(smtp_host, smtp_port, timeout=10)
    try:
        s.login(username, password)
        s.sendmail(msg['From'], username, msg.as_string())
        print('Message Sent.')
    finally:
        s.quit()