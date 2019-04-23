from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.conf import settings

# Create your models here.
class Post(TimeStampedModel):
    # created, modified
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lovers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='bookmarks', blank=True)
