from django.db import models

# Create your models here.

class product(models.Model):
    products=[
        ('electronics', 'electronics'),
        ('garments', 'Garments'),
        ('Food', 'Food'),
        ('Baby Toys', 'Baby Toys'),
        ('other', 'other')
    ]
    product_name=models.CharField(max_length=100)
    product_description=models.CharField(max_length=256)
    product_type=models.TextField(max_length=256, choices=products, default='electronics')
    in_stock=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name