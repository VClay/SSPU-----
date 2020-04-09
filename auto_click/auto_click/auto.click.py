import os
from email import encoders

import requests
from selenium import webdriver
from email.header import Header
from smtplib import SMTP_SSL
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart, MIMEBase
import time

import json
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime
import datetime
from selenium import webdriver

import traceback


def  mail(value):
    sender = "XXXXX@qq.com"  # 发件人邮箱账号
    password = "hytqffnuobcshbei"  # 发件人邮箱密码(当时申请smtp给的口令),百度搜索怎么拿到smtp的qq邮箱密令
    recipient = "@qq.com"  # 收件人邮箱账号

    string = "目前您的报送时间为："


    try:
        msg = MIMEText(string+value, "plain", "utf-8")
        msg["From"] = formataddr(["", sender])
        msg["To"] = formataddr(["", recipient])
        msg["Subject"] = "SSPU每日一报"

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, password)
        server.sendmail(sender, [recipient, ], msg.as_string())
        server.quit()
        return True

    except Exception:
        value="小可爱，你的邮件发送出了点小状况，，请您进入签到历史查看确认。"
        msg = MIMEText(string + value, "plain", "utf-8")
        msg["From"] = formataddr(["", sender])
        msg["To"] = formataddr(["", recipient])
        msg["Subject"] = "SSPU每日一报"

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, password)
        server.sendmail(sender, [recipient, ], msg.as_string())
        server.quit()
        return True
        return False


def main():
    try:
        global driver  # driver = webdriver.Chrome() #设置成了全局变量为的是在捕获异常时候能够调用driver.close()把异常处理掉
        driver = webdriver.Chrome()

        delay = 1  # 设置延时时间0.5s
        driver.get('https://hsm.sspu.edu.cn/selfreport/Default.aspx')
        time.sleep(delay)  # 为保证网络通性不畅导致自动化失败因此设置延时以提高成功率 //
        driver.find_element_by_id('username').send_keys('201XXXX')   #输入账号
        time.sleep(delay)
        driver.find_element_by_name('password').send_keys('sspuXXXX')    #输入密码
        time.sleep(delay)
        driver.find_element_by_class_name('submit_button').click()
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="form1"]/div[6]/ul/li[1]/a/div').click()
        time.sleep(delay)
        driver.find_element_by_class_name('f-btn-text').click()
        time.sleep(delay)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/a[1]/span/span').click() #//*[@id="fineui_31"]/span/span
        time.sleep(delay)  #/html/body/div[3]/div[2]/div[2]/div/div/a
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/a').click()
        time.sleep(delay)
        driver.find_element_by_xpath('/html/body/form/div[6]/ul/li[2]/a/span').click()
        time.sleep(delay)
        msg=driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[1]/div/ul/li[1]/a').text
        print( driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[1]/div/ul/li[1]/a').text)

        driver.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[1]/div/ul/li[1]/a').click()#这个是点进报送历史几面的xpath
        time.sleep(delay)

        driver.close()
        return msg

    except:
        return -1


if __name__ == '__main__':
    print('程序正在运行中哦')

    while(True):
        try:
            index='0'
            curr_time = datetime.datetime.now()
            time_str = datetime.datetime.strftime(curr_time, '%H:%M')
            if(time_str=='04:00'):   #输入需要确认填报的时间，建议在一点以后避免高峰期失败格式XX:XX
                print(time_str)
                index=main()
                if index=='-1' or index=='0':
                    mail('小可爱，您的报错程序出了点小错误哦错误代码{}'.format(index))
                else:
                     mail(index)
                break
            time.sleep(20)#延时20秒
        except:
            print('error')
