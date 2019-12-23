import uuid

from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    category_name = models.CharField(max_length=50, default="")
    category_image = models.ImageField(upload_to="shop/images", default="")


    def __str__(self):
        return self.category_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.category_image.url))

class Product(models.Model):
    class Meta:
        verbose_name_plural = "products"

    id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4, primary_key=True)
    product_category = models.ForeignKey(Category, related_name='product', on_delete='', default="")
    product_name = models.CharField(max_length=50, default="")
    product_image = models.ImageField(upload_to="shop/images", default="")
    product_price = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.product_image.url))

class Slider(models.Model):
    class Meta:
        verbose_name_plural = "sliders"
    slider_image = models.ImageField(upload_to="shop/images", default="")


    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.slider_image.url))