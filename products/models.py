from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_frienldy_name(self):
        return self.friendly_name 

class Product(models.Model):
    name =models.CharField(max_length=100)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_name = models.CharField(max_length=254)
    product_description = models.DecimalField(max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='product_image/')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeginKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    ordered_date = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_place=2)
    order_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f'Order #{self.pk} by {self.user.username}'

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
    
    


  
     
    