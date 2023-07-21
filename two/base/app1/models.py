from django.db import models

# Create your models here.
class app1_customer(models.Model):
    firstName   = models.CharField(max_length=25 , blank=False , null=False)
    secondName  = models.CharField(max_length=25 , blank=False , null=False)
    email       = models.EmailField()
    message     = models.CharField(max_length=25 , blank=False , null=False)
