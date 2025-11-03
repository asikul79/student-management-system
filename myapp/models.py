from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    roll_no=models.CharField(max_length=50,unique=True)
    subject=models.CharField(max_length=100)
    city=models.CharField(max_length=100,default='Hyderabad')
    dob=models.DateField(null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  self.name
