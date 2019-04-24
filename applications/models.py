from django.db import models
from PIL import Image

class application(models.Model):
	application_id = models.IntegerField(primary_key=True, default= 0)
	application_date = models.DateTimeField()
	stu_apps = models.TextField(default=1, max_length=1024*2)
	certificate = models.ImageField(upload_to='leaveApplicaiton/images/')
	user = models.IntegerField()
	flag = models.IntegerField(default=0)
	branch = models.CharField(default='CSE', max_length=5)

	def __str__(self):
		return str(self.user)	


"""
	using epoch timestamp as both application_time and application_id, assuming two people do not submit at the same second
	use:
		from datetime import datetime
		epoch_timestamp = int(datetime.now().timestamp()) 	# This gives unique ID

		# To reverse from epoch_timestamp in human format, use:
		datetime.fromtimestamp(epoch_timestamp).strftime('%d:%b:%Y')

"""
