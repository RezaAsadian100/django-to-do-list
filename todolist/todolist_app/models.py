from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User


class dolist(models.Model):
    title = models.CharField(max_length=100)
    date_edited = models.DateTimeField(auto_now=True)
    content = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
        