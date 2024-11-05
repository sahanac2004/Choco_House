# from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    seasonal = models.CharField(max_length=20, choices=[
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
        ('Winter', 'Winter'),
        ('No season', 'No season'),
    ])
   

    def __str__(self):
        return self.name


class Inventory(models.Model):
    ingredient = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ingredient} - {self.quantity}"


class Suggestion(models.Model):
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    allergies = models.TextField(blank=True)
    def __str__(self):
        return f"Suggestion for {self.flavor.name}"
  
