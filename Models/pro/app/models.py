from django.db import models

class Students(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    details = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    contact = models.IntegerField()


