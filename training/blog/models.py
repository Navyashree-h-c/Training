from django.db import models

class Blog(models.Model):
    name = models.TextField()
    posted_by = models.TextField()
    posted_on = models.DateTimeField()


