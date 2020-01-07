from django.db import models
class employeemodels(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    eposition=models.CharField(max_length=100)
    eaddress=models.CharField(max_length=100)
    eproject=models.CharField(max_length=100)
    esalary=models.FloatField()
    eusername=models.CharField(max_length=100)
    epassword=models.CharField(max_length=10)
    eemail=models.EmailField(max_length=100)
    esal=models.IntegerField(default=True)
