from tkinter import CASCADE
from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=40)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

class Drinks(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    class Meta:
        db_table = 'drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=40)
    drinks = models.ManyToManyField('Drinks', through='allergydrink')

    class Meta:
        db_table = 'allergy'

class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drinks = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergydrink'

class Image(models.Model):
    image_url = models.URLField(max_length=2000, null = True)
    drinks = models.ForeignKey('Drinks', on_delete=models.CASCADE)

    class Meta:
        db_table = 'image'