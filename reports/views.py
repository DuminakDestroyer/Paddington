from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Report

def home(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect("dashboard")
		else:
			return render(request, 'fragments/error.html', {})
	if request.user.is_authenticated():
		return redirect("dashboard")
	return render(request, 'fragments/login.html', {})


def dashboard(request):
	if not request.user.is_authenticated:
		return redirect('home')
	return render(request, 'fragments/home.html', {})


def logout_view(request):
	logout(request)
	return redirect("home")


def upload(request):
	if not request.user.is_authenticated:
		return redirect('home')
	return render(request, 'fragments/upload.html', {})


def report(request):
	if not request.user.is_authenticated:
		return redirect('home')
	reports = Report.objects.all()
	return render(request, 'fragments/report.html', {'reports': reports})