from django.db import models


class Catagory(models.Model):
    title = models.CharField(max_length=250)
    feature_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+',blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(default='-')
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']


class Like(models.Model):
    like = models.PositiveSmallIntegerField()
    product = models.OneToOneField(Product,on_delete=models.CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200,null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
        

class Address(models.Model):
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250,null=True)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED =  'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_COMPLETE,'Complete'),
        (PAYMENT_FAILED,'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unite_price = models.DecimalField(max_digits=7,decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()




