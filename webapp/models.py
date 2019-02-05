from django.db import models


class Patient(models.Model):
    adhaarId = models.IntegerField()
    fname = models.CharField(max_length=20)
    sname = models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname