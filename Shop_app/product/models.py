from django.db import models
from account.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=250, null=True, blank=True)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to = 'product_image')
    product_price = models.PositiveIntegerField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="author")
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return f"{self.product_name} - {self.product_description}"