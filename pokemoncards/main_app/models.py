from django.db import models

class Pokemon(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    power=models.IntegerField()
    weakness=models.CharField(max_length=100)
    image= models.ImageField(upload_to='main_app/static/uploads',default='')
    def __str__(self):
        return self.name
# Create your models here.
