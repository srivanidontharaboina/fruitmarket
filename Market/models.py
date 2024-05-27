from django.db import models

# Create your models here.
class Fruit(models.Model):
    fruit_name=models.CharField(max_length=50)
    scientific_name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='images')
    season=models.CharField(max_length=50)
    price=models.CharField(max_length=3)
    def __str__(self):
        return self.fruit_name