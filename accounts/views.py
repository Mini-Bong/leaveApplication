from django.shortcuts import render, redirect
from .models import student_acc, hod_acc
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings


def nav(request):
	if not request.session.get('logged') == True:
		return render(request, 'accounts/nav.html')
	else:
		return redirect('home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
	if not request.session.get('logged') == True:
		if request.method == 'POST':
			reg_no = request.POST['reg']
			password = request.POST['psw']
			if student_acc.objects.filter(reg=reg_no).exists():
				stu_ins = student_acc.objects.get(reg=reg_no)
				if stu_ins.password == password:
					request.session['logged'] = True
					request.session['reg_session'] = reg_no
					return redirect('home')
				else:
					return render(request, 'accounts/login.html',{'msg':'you have enter wrong password'})
			else:
				return render(request, 'accounts/login.html',{'msg':'you have enter wrong username'})
		else:
			return render(request, 'accounts/login.html')
	else:
		return redirect('home')


def signup(request):
	if request.method == 'POST':
		reg_no = request.POST['reg']
		name = request.POST['name']
		branch = request.POST['branch']
		mail = request.POST['mail']
		password = request.POST['password']
		if student_acc.objects.filter(reg=reg_no).exists():
			return render(request, 'accounts/signUp.html',{'flag':'Registration number already exists'})
		else:
			new_account = student_acc.objects.create(reg=reg_no, name=name, branch=branch, mail=mail, password=password)
			new_account.save()
			return render(request, 'accounts/signUp.html',{'flag':'Registration successful, Go for login'})
	else:
		return render(request, 'accounts/signUp.html')	

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def HOD(request):
	if request.method == 'POST':
		if request.POST.get('submit')=='REGISTER':
			mail = request.POST['email']
			password = request.POST['Password']
			name = request.POST['Name']
			branch = request.POST['Branch']
			mobile = request.POST['mobile_No']
			if hod_acc.objects.filter(email=mail).exists():
				return render(request, 'accounts/HOD.html',{'flag':'Email already exists'})
			else:
				new_account = hod_acc.objects.create(email=mail, hod_name=name, branch_name=branch, mobile_no=mobile, psw=password)
				return render(request, 'accounts/HOD.html',{'flag':'Registration successful, Go for login'})
				new_account.save()
		elif request.POST.get('submit')=='LOGIN':
			if not request.session.get('logged')==True:
				mail = request.POST['Email']
				password = request.POST['password']
				if hod_acc.objects.filter(email=mail).exists():
					hod_ins = hod_acc.objects.get(email=mail)
					if hod_ins.psw == password:
						if hod_ins.branch_name == "CSE":
							return redirect('hod_CSE')
						elif hod_ins.branch_name == "EEE":
							return redirect('hod_EEE')
						elif hod_ins.branch_name == "ECE":
							return redirect('hod_ECE')
						elif hod_ins.branch_name == "EIE":
							return redirect('hod_EIE')
						elif hod_ins.branch_name == "Civil":
							return redirect('hod_Civil')
						else:
							return redirect('hod_Mech')			
					else:
						return render(request, 'accounts/HOD.html',{'msg':'Incorrect password'})
				else:
					return render(request, 'accounts/HOD.html',{'msg':'invalid username'})
			else:
				return redirect('hod_path')
		else:
			return render(request, 'accounts/HOD.html')
	else:
		return render(request, 'accounts/HOD.html')

def logout(request):
	request.session.clear()
	return redirect('nav')

def logout_hod(request):
	request.session.clear()
	return redirect('HOD')


def resetpsw(request):
	if request.method == 'POST':
		mail = request.POST['mail']
		if student_acc.objects.filter(mail=mail).exists():
			subject = 'Password request'
			student_instance = student_acc.objects.get(mail=mail)
			body = student_instance.password
			sent_from = 'settings.EMAIL_HOST_USER'
			to = request.POST['mail']
			send_mail(subject, body, 'sent_from', [to, ])
			return render(request,'accounts/forgot_pwd.html')
		else:
			return render(request, 'accounts/forgot_pwd.html', {'flag':'Email not register'})
	else:
		return render(request,'accounts/forgot_pwd.html')
	

