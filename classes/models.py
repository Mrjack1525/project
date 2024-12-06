# models.py
from django.db import models

class contactus(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"

    class meta:
        db="classes_contactus"