from django.db import models

from projects.models import Project

class Task(models.Model):
	STATUSES = (
		('new','Новая'),
		('in_development', 'В разработке'),
		('close','Закрыта'),
		('cancel','Отменено'),
	)

	name = models.CharField(max_length=60)
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.CharField(max_length=50, choices=STATUSES, default='new')
	project = models.ForeignKey(Project, null=True, blank=True)

	def __str__(self):
		return self.name

class Comments(models.Model):
	class Meta():
		db_table = 'comments'

	comments_text = models.TextField()
	comments_article = models.ForeignKey(Task)