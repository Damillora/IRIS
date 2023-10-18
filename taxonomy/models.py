from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="logo",blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
class Unit(models.Model):
    name = models.CharField(max_length=255,blank=True)
    area = models.OneToOneField("Area",on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name