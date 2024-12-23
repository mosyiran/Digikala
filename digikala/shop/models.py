from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default= 1)
    picture = models.ImageField( upload_to='upload/product/')

    # SIZE_HA = (
    #     ('m',32),
    #     ('l',42),
    #     ('xl',52)
    #
    # )
    # size = models.CharField(max_length=4, choices=SIZE_HA, default=32)
    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name




