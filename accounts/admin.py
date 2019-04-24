from django.contrib import admin
from .models import student_acc
from .models import hod_acc

admin.site.register(student_acc)
admin.site.register(hod_acc)