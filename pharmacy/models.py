from django.db import models

class Prescription(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    prescription_details = models.TextField()

    def __str__(self):
        return self.full_name
