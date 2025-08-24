from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"


class SparePart(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="spare_parts")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/sparparts_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.car}"