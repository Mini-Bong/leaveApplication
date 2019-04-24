from django.db import models

class student_acc(models.Model):
	reg = models.IntegerField(primary_key=True)
	name = models.CharField(null=True, max_length=20)
	branch = models.CharField(max_length=3, null=True)
	mail = models.CharField(max_length=20, null=True)
	password = models.CharField(max_length=10, null=True)


	def __str__(self):
		return str(self.reg)

class hod_acc(models.Model):
	email = models.CharField(primary_key=True, max_length=30)
	psw = models.CharField(null=True, max_length=20)
	hod_name = models.CharField(null=True, max_length=20)
	branch_name = models.CharField(max_length=3, null=True)
	mobile_no = models.IntegerField(null=True)

	def __str__(self):
		return str(self.hod_name)