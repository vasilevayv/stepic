from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.order_by('-rating')

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateField(blank=True, auto_now_add=True)
  rating = models.IntegerField(default=0)
  author = models.ForeignKey(User,
                            null = True, on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User, related_name='likes_set')
  objects = QuestionManager()
  
class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField(blank=True, auto_now_add=True)
  question = models.ForeignKey(Question,
                              on_delete=models.CASCADE)
  author = models.ForeignKey(User,
			null=True, on_delete=models.SET_NULL)
