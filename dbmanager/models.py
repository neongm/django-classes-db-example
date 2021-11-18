from django.db import models

# Create your models here.

class Article(models.Model):
    # id = models.AutoField(primary_key=True) - here by default
    author_name = models.CharField('author name', max_length=100, default="None")
    title = models.CharField('record title', max_length=200)
    text = models.TextField('record text')

    def __str__(self):
        return self.title

