# from itertools import product
from django.db import models
from users.models import User
from products.models import product
from Cart.models import Cart
# Create your models here.

class Order(models.Model):
    order_choices=[

        ('pending','pending'),
        ('confirmed','confirmed'),
        ('shipped','shipped'),
        ('delivered','delivered'),
        ('cancelled','cancelled'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, choices=order_choices, default=('pending'))
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"
    
