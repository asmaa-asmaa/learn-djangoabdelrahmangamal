from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    x=[('phone','phone'),
       ('computer', 'computer')]
    name = models.CharField(max_length= 50, default='asmaa',verbose_name='title')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # content = models.TextField(default='description')
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos\24\11\21\landing_page_returant.png')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices= x)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'prod'
        ordering = ['name']

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    #created = models.DateTimeField(null=True)
    created = models.DateTimeField(default=datetime.now)