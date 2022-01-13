from django.db import models

# Create your models here.
class Customer(models.Model):
    profile = models.CharField(max_length= 20)
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=10,)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.username

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False