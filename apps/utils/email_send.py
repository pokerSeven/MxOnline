# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/7/27 2:33'
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM

def random_str(randomlength=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str += chars[random.randint(0, length)]
	return str


def send_register_email(email, send_type="register"):
	email_record = EmailVerifyRecord()
	code = random_str(16)
	email_record.code = code
	email_record.email = email
	email_record.send_type = "register"
	email_record.save()

	email_title = ""
	email_boby = ""

	if send_type == "register":
		email_title = "慕学在线网注册激活链接"
		email_boby = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

		send_status = send_mail(email_title,email_boby,EMAIL_FROM,[email])
		if send_status:
			pass

