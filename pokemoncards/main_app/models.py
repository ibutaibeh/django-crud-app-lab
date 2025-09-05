from django.db import models
from django.urls import reverse
RARITY=(
    ('R','Rare'),
    ('SR','Super Rare'),
    ('UR','Ultra Rare')
)

class Accessory(models.Model):
    name= models.CharField(max_length=50)
    color= models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('accessory_detail',kwargs={'pk':self.id})
    
    
class Pokemon(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    power=models.IntegerField()
    weakness=models.CharField(max_length=100)
    image= models.ImageField(upload_to='main_app/static/uploads',default='')
    accessories= models.ManyToManyField(Accessory) 
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('details',kwargs={'pokemon_id':self.id})
# Create your models here.

class Purchase(models.Model):
    date=models.DateField()
    rarity=models.CharField(max_length=3, choices=RARITY, default=RARITY[0][0])
    pokemon= models.ForeignKey(Pokemon,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.pokemon.name} {self.get_rarity_display()} on {self.date}"