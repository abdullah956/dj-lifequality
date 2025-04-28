from django.db import models
from config.models import BasedModel

class Category(BasedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Product(BasedModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredient = models.TextField(blank=True, null=True)
    how_to_use = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    best_sellers = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)
    hot_sales = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    def __str__(self):
        return self.name


class Review(BasedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.product.name}"