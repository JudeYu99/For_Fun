# -*- coding: utf-8 -*-

"""
Sending e-mails automatically

@author: Yu Zhu
"""

def send_mail(mail_info):
    """
  
    Parameters
    ----------
    mail_info : dict
        sender_mail : str
        pwd : str
        receiver_mail : str
        mail_title : str
        mail_content : str

    Returns
    -------
    None.

    """
    
    from email.mime.text import MIMEText
    from email.header import Header
    from smtplib import SMTP_SSL
    
    mail = ["sender_mail", "pwd", "receiver_mail", "mail_title", "mail_content"]
    for key in mail:
        if key in mail_info:
            pass
        else:
            raise Exception("Parameter in need: %s"%key)
    
    sender_mail = mail_info["sender_mail"]
    pwd = mail_info["pwd"]
    receiver_mail = mail_info["receiver_mail"]
    mail_title = mail_info["mail_title"]
    mail_content = mail_info["mail_content"]
    
    # QQ mail server
    host_server = 'smtp.qq.com'
    
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)

    smtp.login(sender_mail, pwd)
    
    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_mail
    msg["To"] = receiver_mail
    smtp.sendmail(sender_mail, receiver_mail, msg.as_string())
    smtp.quit()


mail_info = {"sender_mail": "SENDER@qq.com", "pwd": "PASSWORD", "receiver_mail": "RECEIVER@qq.com", "mail_title": "MY_TITLE", "mail_content": "MY_CONTENT"}

'''
for i in range(10):
    send_mail(mail_info)
'''
