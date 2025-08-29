from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/cars',blank=True,null=True)

    def __str__(self):
        return f"{self.make} "

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class SparePart(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="spare_parts")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_spare_parts",null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.car}"