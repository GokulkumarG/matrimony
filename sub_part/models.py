from django.db import models

# Create your models here.
class register_data(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    date_birth=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    study=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    file=models.ImageField(upload_to='images/')
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.gender
   
    
class login_data(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=50)
    
class admin_data(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class deleted_data(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    date_birth=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    study=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    file=models.ImageField(upload_to='images/')
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=50,null=True)
    
    