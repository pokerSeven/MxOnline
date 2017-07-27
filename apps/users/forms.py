# _*_ coding: utf-8 _*_
__author__ = 'lhj'
__date__ = '2017/7/26 22:42'
from  django import forms
from captcha.fields import  CaptchaField

class LoginForm(forms.Form):
	username = forms.CharField(required=True,min_length=3)
	password = forms.CharField(required=True)

class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True,min_length=5)
	captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})



