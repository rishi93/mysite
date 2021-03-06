from django.db import models
from django.utils import timezone
#Upload image files to Cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class Question(models.Model):
	picture = CloudinaryField('image', blank=True, null = True)
	if_picture = models.BooleanField(default=False)
	question_text = models.TextField()
	created_at = models.DateTimeField()
	author = models.ForeignKey('auth.User')
	upvotes = models.ManyToManyField('auth.User', blank=True, related_name='upvotes')
	downvotes = models.ManyToManyField('auth.User', blank=True, related_name='downvotes')

	def __str__(self):
		return self.question_text

class Comment(models.Model):
	question = models.ForeignKey('myapp.Question', related_name='comments')
	comment_text = models.TextField()
	created_at = models.DateTimeField()
	author = models.ForeignKey('auth.User')

	def __str__(self):
		return self.comment_text
