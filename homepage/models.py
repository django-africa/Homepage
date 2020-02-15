from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
     first_name = models.CharField(max_length=60)
     last_name = models.CharField(max_length=60)
     email = models.EmailField(max_length=254)
     subject = models.CharField(max_length=120)
     message = models.TextField()
     submited_date = models.DateTimeField(auto_now_add=True)