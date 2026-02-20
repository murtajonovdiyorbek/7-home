from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Mechanic(models.Model):
    full_name = models.CharField(max_length=255)
    experience_year = models.IntegerField()
    phone = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Service(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name