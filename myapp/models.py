from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text = models.TextField()
	created_at = models.DateTimeField(default = timezone.now())
	author = models.ForeignKey('auth.User')

	def __str__(self):
		return self.question_text
