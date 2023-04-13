from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name=models.CharField(max_length=255, db_index=True, null=True)
    slug=models.SlugField(max_length=255, unique=True, null=True)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:Categorylist', args=[self.slug])
    
class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    author=models.CharField(max_length=200, default='admin')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_creator', null=True)
    title=models.CharField(max_length=200, null=True)
    image=models.ImageField(upload_to='images/', null=True)
    slug=models.SlugField(max_length=200, unique=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2, null=True)
    inStock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    objects=models.Manager()
    products=ProductManager()

    class Meta:
        verbose_name_plural='products'
        ordering=('-created',)
    
    def get_absolute_url(self):
        return reverse('store:Productdetail', args=[self.slug])
    
    def __str__(self):
        return self.title



