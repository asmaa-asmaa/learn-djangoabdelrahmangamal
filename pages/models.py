from django.db import models

# Create your models here.
class Female(models.Model):
    name_female = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.name_female
class Male(models.Model):
    name_male = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.name_male
    girls = models.OneToOneField(Female, on_delete=models.CASCADE)
   # girls = models.OneToOneField(Female, on_delete=models.PROTECT)



class Product(models.Model):
    title = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.title
    

class User(models.Model):
    name= models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.name
    products= models.ForeignKey(Product, on_delete=models.CASCADE)    

class Video(models.Model):
    title = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.title
    

class UserName(models.Model):
    name= models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.name
    watch = models.ManyToManyField(Video)

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)