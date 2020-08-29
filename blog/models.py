from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_text = HTMLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    post_datetime = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-id"]