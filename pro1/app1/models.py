from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,MaxValueValidator,MinValueValidator,EmailValidator
from app1.validation import validate_name

# Create your models here.

class Person(models.Model):
    name=models.CharField(max_length=100,validators=[validate_name])
    age=models.IntegerField(validators=[MaxValueValidator(70),MinValueValidator(18)])
    email=models.EmailField(unique=True,validators=[EmailValidator])
    contact=models.CharField(max_length=10,null=True)
    address=models.CharField(blank=True,null=True,max_length=255,validators=[MaxLengthValidator(255),MinLengthValidator(10)])
    username=models.CharField(unique=True,max_length=100,null=True)
    password=models.CharField(unique=True,max_length=100,null=True)
    image=models.ImageField(upload_to='Image/User_image')


    def __str__(self) -> str:
        return self.name
    

       

class Customer(models.Model):
    C_name=models.CharField(max_length=255,validators=[validate_name])
    C_address=models.CharField(max_length=255,validators=[MaxLengthValidator(255),MinLengthValidator(10)])
    C_contact=models.BigIntegerField(null=False,blank=False,unique=True)
    C_email=models.EmailField(unique=True,blank=False,null=False,validators=[EmailValidator])
    C_age=models.IntegerField(validators=[MaxValueValidator(70),MinValueValidator(18)])
    C_image=models.ImageField(upload_to='Image/customer_image')

    def __str__(self) -> str:
        return self.C_name
    
  