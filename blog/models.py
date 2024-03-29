from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content

