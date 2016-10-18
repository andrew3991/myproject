from django.db import models
from django.conf import settings

class Project(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	name = models.CharField(max_length=60)
	start_date = models.DateField()
	end_date = models.DateField()
	

	def __str__(self):
		return self.name
