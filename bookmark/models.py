from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('site url')
    def __str__(self):
        return self.site_name + "(" + self.url + ")"