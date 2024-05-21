from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122, null=False)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return f"{self.name}"
    
class Appointment(models.Model):
    name=models.CharField(max_length=122)
    age=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.EmailField(max_length=200)
    department=models.CharField(max_length=122)
    address=models.TextField()
    date=models.CharField(max_length=122)
    time=models.CharField(max_length=122)
    doctor=models.CharField(max_length=50)
    slot=models.CharField(max_length=10)
    bmi=models.CharField(max_length=5)
    day=models.CharField(max_length=5)
    summary=models.CharField(max_length=122)
    report =models.ImageField(upload_to='satic/img',verbose_name='report')

    def __str__(self):
        return f"{self.name}"

class Bookings(models.Model):
    doctor=models.CharField(max_length=50)
    day=models.CharField(max_length=5)
    slot=models.CharField(max_length=10)
    patient_name=models.CharField(max_length=122)
    
    


    def __str__(self):
        return f"{self.doctor}"
    
    