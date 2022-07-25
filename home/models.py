from django.db import models

# Create your models here.
categories = {
    ("Laptop","Laptop"),
    ("Printer","Printer"),
    ("Desktop","Desktop"),
    ("Accessories","Accessories")
}

class Product(models.Model):
    category=models.CharField(choices=categories,max_length=50)
    model_name=models.CharField(max_length=100)
    specification=models.TextField()
    price = models.PositiveIntegerField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.category} - {self.model_name}"

    
    class Meta:
        ordering = ['-published_at']

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.product} - {self.name} - {self.ordered_at.year}-{self.ordered_at.month}-{self.ordered_at.day}"

    class Meta:
        ordering = ['-ordered_at']