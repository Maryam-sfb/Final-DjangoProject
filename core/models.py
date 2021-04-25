from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')  # many to one
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')  # many to one
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')  # many to one
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
