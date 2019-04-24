from django.shortcuts import render, redirect
from accounts.models import student_acc
from .models import application
from django.views.decorators.cache import cache_control
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def userhome(request):
	registration = request.session['reg_session']
	if request.method == 'POST':
		date = request.POST['Date']
		file = request.FILES['myfile']
		stuApplication  = request.POST['application']
		flag = 0
		stu_ins = student_acc.objects.get(reg=registration)
		app_id = application.objects.all().order_by('application_id').last()
		new_account = application.objects.create(application_id=app_id.application_id + 1, application_date=date, stu_apps=stuApplication, certificate=file, user=registration, flag = flag, branch=stu_ins.branch)
		new_account.save()
		return render(request, 'accounts/sucessefully.html', {'msg':'application sucessefully'})
	else:
		reg_no = request.session['reg_session']
		student_instance = student_acc.objects.get(reg=reg_no)
		data = {}
		data['stu_name'] = student_instance.name
		data['stu_reg'] = reg_no
		data['stu_branch'] =  student_instance.branch
		return render(request, 'accounts/main.html', {'data':data})


def hod_CSE(request):
	if request.method == 'POST':
		if 'reg' in request.POST:
				app_id = request.POST['reg']
				request.session['reg_session'] = app_id
				student_app = application.objects.get(application_id=app_id)
				#return render(request,'accounts/application.html', {'student_app':student_app})
				return redirect('app')
		elif 'reg1' in request.POST:
				app_id = request.POST['reg1']
				request.session['reg_session'] = app_id
				student_app = application.objects.get(application_id=app_id)
				return render(request,'accounts/accepted_app.html', {'student_app':student_app})
		elif 'reg2' in request.POST:
				app_id = request.POST['reg2']
				request.session['reg_session'] = app_id
				student_app = application.objects.get(application_id=app_id)
				return render(request,'accounts/accepted_app.html', {'student_app':student_app})
			

	else:
		stu_application = application.objects.all().filter(branch="CSE").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})



def hod_EEE(request):
	if request.method == 'POST':
		app_id = request.POST['reg']
		request.session['reg_session'] = app_id
		student_app = application.objects.get(application_id=app_id)
		#return render(request,'accounts/application.html', {'student_app':student_app})
		return redirect('app')
	else:
		stu_application = application.objects.all().filter(branch="EEE").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})

def hod_ECE(request):
	if request.method == 'POST':
		app_id = request.POST['reg']
		request.session['reg_session'] = app_id
		student_app = application.objects.get(application_id=app_id)
		#return render(request,'accounts/application.html', {'student_app':student_app})
		return redirect('app')
	else:
		stu_application = application.objects.all().filter(branch="ECE").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})

def hod_EIE(request):
	if request.method == 'POST':
		app_id = request.POST['reg']
		request.session['reg_session'] = app_id
		student_app = application.objects.get(application_id=app_id)
		#return render(request,'accounts/application.html', {'student_app':student_app})
		return redirect('app')
	else:
		stu_application = application.objects.all().filter(branch="EIE").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})

def hod_Civil(request):
	if request.method == 'POST':
		app_id = request.POST['reg']
		request.session['reg_session'] = app_id
		student_app = application.objects.get(application_id=app_id)
		#return render(request,'accounts/application.html', {'student_app':student_app})
		return redirect('app')
	else:
		stu_application = application.objects.all().filter(branch="CIVIL").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})

def hod_Mech(request):
	if request.method == 'POST':
		app_id = request.POST['reg']
		request.session['reg_session'] = app_id
		student_app = application.objects.get(application_id=app_id)
		#return render(request,'accounts/application.html', {'student_app':student_app})
		return redirect('app')
	else:
		stu_application = application.objects.all().filter(branch="MECH").order_by('application_id')
		return render(request, 'accounts/AppilicationFormIndex.html', {'stu_application':stu_application})

def app(request):
	app_id = request.session['reg_session']
	if request.method == 'POST':
		if request.POST['app'] == 'Accept':
			student_app = application.objects.get(application_id=app_id)
			student_app.flag = 1
			student_app.save()
			subject = 'Leave Application Status'
			reg = student_app.user
			body = 'your leave application is accepted'
			from_mail = 'settings.EMAIL_HOST_USER'
			student_instance = student_acc.objects.get(reg=reg)
			to = student_instance.mail
			send_mail(subject, body, from_mail, [to,])
			if student_instance.branch == "CSE":
				return redirect('hod_CSE')
			elif student_instance.branch == "EEE":
				return redirect('hod_EEE')
			elif student_instance.branch == "ECE":
				return redirect('hod_ECE')
			elif student_instance.branch == "EIE":
				return redirect('hod_EIE')
			elif student_instance.branch == "Civil":
				return redirect('hod_Civil')
			else:
				return redirect('hod_Mech')	 
		elif request.POST['app'] == 'Reject':
			student_app = application.objects.get(application_id=app_id)
			student_app.flag = 2
			student_app.save()
			subject = 'Leave Application Status'
			reg = student_app.user
			body = 'your leave application is rejected'
			from_mail = 'settings.EMAIL_HOST_USER'
			student_instance = student_acc.objects.get(reg=reg)
			to = student_instance.mail
			send_mail(subject, body, from_mail, [to,])
			if student_instance.branch == "CSE":
				return redirect('hod_CSE')
			elif student_instance.branch == "EEE":
				return redirect('hod_EEE')
			elif student_instance.branch == "ECE":
				return redirect('hod_ECE')
			elif student_instance.branch == "EIE":
				return redirect('hod_EIE')
			elif student_instance.branch == "Civil":
				return redirect('hod_Civil')
			else:
				return redirect('hod_Mech')
		elif request.POST['app'] == "Under observation":
			student_app = application.objects.get(application_id=app_id)
			student_app.flag = 3
			student_app.save()
			subject = 'Leave Application Status'
			reg = student_app.user
			body = 'your leave application is kept in observation'
			from_mail = 'settings.EMAIL_HOST_USER'
			student_instance = student_acc.objects.get(reg=reg)
			to = student_instance.mail
			send_mail(subject, body, from_mail, [to,])
			if student_instance.branch == "CSE":
				return redirect('hod_CSE')
			elif student_instance.branch == "EEE":
				return redirect('hod_EEE')
			elif student_instance.branch == "ECE":
				return redirect('hod_ECE')
			elif student_instance.branch == "EIE":
				return redirect('hod_EIE')
			elif student_instance.branch == "Civil":
				return redirect('hod_Civil')
			else:
				return redirect('hod_Mech')
		else:
			student_app = application.objects.get(application_id=app_id)
			request.session['data_id']=student_app.application_id
			return redirect('show_app')
	else:
		student_app = application.objects.get(application_id=app_id)
		return render(request,'accounts/application.html', {'student_app':student_app})

def show_app(request):
	return render(request, 'accounts/accepted_app.html')