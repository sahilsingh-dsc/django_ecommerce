from django.contrib import admin
from .models import  Category, Product, Slider

admin.site.register(Category, list_display=['category_name', 'image_tag'])
admin.site.register(Product, list_display=['id', 'product_image', 'product_name', 'product_price', 'product_desc', 'product_category', 'image_tag'])
admin.site.register(Slider, list_display=['image_tag'])

# Register your models here.

