# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

# Create your views here.

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm
from utils.email_send import send_register_email


class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
			user = UserProfile.objects.get(Q(username=username) | Q(email=username))
			if user.check_password(password):
				return user
		except Exception as e:
			return None


class LoginView(View):
	def get(self, request):
		return render(request, "login.html", {})

	def post(self, request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user_name = request.POST.get("username", "")
			pass_word = request.POST.get("password", "")
			user = authenticate(username=user_name, password=pass_word)
			if user is not None:
				login(request, user)
				return render(request, "index.html")
			else:
				return render(request, "login.html", {"msg": u"用户名或密码错误"})
		else:
			return render(request, "login.html", {"login_form": login_form})


class ActiveUserView(View):
	def get(self, request, active_code):
		all_records = EmailVerifyRecord.objects.filter(code= active_code)
		if all_records:
			for record in all_records:
				email = record.email
				user = UserProfile.objects.get(email=email)
				user.is_active = True
				user.save()


class RegisterView(View):
	def get(self, request):
		register_form = RegisterForm()
		return render(request, "register.html", {"register_form": register_form})

	def post(selfs, request):
		register_form = RegisterForm()
		if register_form.is_valid():
			user_name = request.POST.get("email", "")
			pass_word = request.POST.get("password", "")
			user_profile = UserProfile()
			user_profile.username = user_name
			user_profile.email = user_name
			user_profile.is_active = False
			user_profile.password = make_password(pass_word)
			user_profile.save()

			send_register_email(user_name, "register")
			return render(request, "login.html")
		else:
			return render(request, "register.html", {"register_form": register_form})
