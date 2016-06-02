import unittest,time
from HTMLTestRunner import HTMLTestRunner
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#from email.header import header
#import smtplib
#import os

# #===============定义发送邮件===========================
# def send_mail(file_new):
#   f = open(file_new,'rb')
#   mail_body = f.read()
#   f.close()

#   msg = MIMEText(mail_body,'html','utf-8')
#   msg['Subject'] = header("自动化测试报告",'utf-8')

#   smtp = smtplib.SMTP()

#指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'test_*.py')

if __name__ == '__main__':
  now = time.strftime("%Y-%m-%d %H_%M_%S")
  filename = test_dir + '/' + now + 'result.html'
  fp = open(filename,'wb')
  runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况: ')
  runner.run(discover)
  fp.close()
