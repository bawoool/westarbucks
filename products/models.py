from tkinter import CASCADE
from django.db import models

# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'menu'

class category(models.Model):
    name = models.CharField(max_length=40)
    menu = models.ForeignKey('menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

class drinks(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey('category', on_delete=models.CASCADE)


    class Meta:
        db_table = 'drinks'

class allergy(models.Model):
    name = models.CharField(max_length=40)
    drinks = models.ManyToManyField(drinks, through='allergydrink')

    class Meta:
        db_table = 'allergy'

class allergydrink(models.Model):
    allergy = models.ForeignKey(allergy, on_delete=models.CASCADE)
    drinks = models.ForeignKey(drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergydrink'

class image(models.Model):
    image_url = models.URLField(max_length=200)
    drinks = models.ForeignKey(drinks, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image'