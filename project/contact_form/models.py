from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=300)