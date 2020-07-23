from django.db import models

from datetime import datetime

class Comment(models.Model):
        email = models.EmailField()
        content = models.CharField(max_length=200)
        created_at = models.DateTimeField(auto_now=True)
