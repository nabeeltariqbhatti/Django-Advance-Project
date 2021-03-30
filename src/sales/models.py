from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone


class Position(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id:{self.id}, product:{self.product.name}, quantity:{self.quantity}"

    def save(self, *args, **kwargs):
        if self.transavtion_id == "":
            self.transaction_id = ''
        if self.created_at is None:
            self.created_at = timezone.now()
            return super().save(*args, **kwargs)

    def get_positions(self):
        return self.postions.all()


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sales for the amount of ${self.total_price}"


class CSV(models.Model):
    file_name=models.FileField(upload_to='csvs')
    activated=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
