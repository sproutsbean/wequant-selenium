#!/user/bin/env python
# -*-coding:utf-8-*-
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from smtplib import SMTP_SSL
import smtplib


def sendmail(mail_title, mail_content, sender_qq_mail='282751606@qq.com', receiver='lijie@huobi.com'):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = '282751606'
    # pwd为qq邮箱的授权码
    pwd = 'wtwlsjhdkihgcbec'
    # 发件人的邮箱
    sender_qq_mail = sender_qq_mail
    # 收件人邮箱
    receiver = receiver
    # 邮件的正文内容
    mail_content = mail_content
    # 邮件标题
    mail_title = mail_title

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


def sendHtmlEmail(picname):
    sender = '282751606@qq.com'
    receiver = 'lijie@huobi.com'
    subject = 'python email test'
    smtpserver = 'smtp.qq.com'
    username = '282751606'
    password = 'wtwlsjhdkihgcbec'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '实盘数据加载失败，请注意查看原因！'

    msgText = MIMEText('<b>运行失败截图</b> <br><img src="cid:image1"><br>', 'html', 'utf-8')
    msgRoot.attach(msgText)

    fp = open(picname, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    # ssl登录
    smtp = SMTP_SSL(smtpserver)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print "Successful"

def sendmailatt(mail_title, mail_content, sender_qq_mail='282751606@qq.com', receiver='lijie@huobi.com'):
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = '282751606'
    # pwd为qq邮箱的授权码
    pwd = 'wtwlsjhdkihgcbec'
    # 发件人的邮箱
    sender_qq_mail = sender_qq_mail
    # 收件人邮箱
    receiver = receiver
    # 邮件的正文内容
    mail_content = mail_content
    # 邮件标题
    mail_title = mail_title

    # ssl登录
    smtp = SMTP_SSL(host_server)
    # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(0)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver

    # 构造附件
    att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="1.jpg"'
    msg.attach(att)
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()
