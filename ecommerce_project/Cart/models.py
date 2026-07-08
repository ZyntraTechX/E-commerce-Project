from django.db import models
from users.models import User
from products.models import product
# Create your models here.

class Cart(models.Model):
    # cart=models.OneToOneField(User, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=('user', 'product')
        
    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"
    
    

