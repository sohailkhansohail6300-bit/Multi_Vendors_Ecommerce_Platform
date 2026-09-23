from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):

    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('home_living', 'Home & Living'),
        ('beauty', 'Beauty'),
        ('sports', 'Sports'),
        ('grocery', 'Grocery'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('automotive', 'Automotive'),
        ('health', 'Health'),
        ('jewelry', 'Jewelry'),
        ('baby_products', 'Baby Products'),
        ('pet_supplies', 'Pet Supplies'),
        ('office_supplies', 'Office Supplies'),
        ('gaming', 'Gaming'),
    ]

    name = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        unique=True
    )

    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    Name=models.CharField(max_length=50)
    Description=models.TextField()
    Price=models.DecimalField(max_digits=7, decimal_places=2)
    image=models.ImageField(upload_to="product_images", height_field=None, width_field=None, max_length=None)
    category_relation=models.ForeignKey(Category,on_delete=models.CASCADE)
    user_relation=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
    
class Quantity(models.Model):
    qty=models.IntegerField()
    product_relation=models.ForeignKey(Product,on_delete=models.CASCADE)


class Review(models.Model):
    review_text = models.TextField()
    product_relation = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_relation = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_relation.username} for {self.product_relation.Name}"


class Oreder(models.Model):
    product_relation = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_relation = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=30)
    shipping_address=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone=models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} x {self.product_relation.Name} by {self.user_relation.username}"

