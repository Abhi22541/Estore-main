from django.contrib import admin
from .models import*
# Register your models here.
class Categoryadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

class Productadmin(admin.ModelAdmin):
    list_display=['title', 'author', 'slug', 'price','inStock', 'created', 'updated']
    list_filter=['inStock', 'is_active']
    list_editable=['price', 'inStock']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category, Categoryadmin)
admin.site.register(Product, Productadmin)
