from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    
    OCCUPATION_CHOICES = [
        ('Branch Leader', 'Branch Leader'),
        ('A-Team', 'A-Team'),
        ('Z-Team', 'Z-Team'),
    ]
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    status = models.CharField(max_length=50, default='Active') # e.g. Active, Injured
    power = models.CharField(max_length=200)
    
    # We store just the filename (e.g. "phenomaman.webp")
    image_filename = models.CharField(max_length=100) 
    description = models.TextField()

    def __str__(self):
        return self.name
