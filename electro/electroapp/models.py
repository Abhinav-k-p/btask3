from django.db import models
from django.contrib.auth.models import User

# Define the choices for the state field
STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),  # Corrected the spelling here
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Daman and Diu', 'Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),  # Corrected the spelling here
    ('Haryana', 'Haryana'),
    ('Kerala', 'Kerala'),
    
)

CATEGORY_CHOICES = (
    ('CR', 'TV'),
    ('ML', 'MOBILE'),
    ('LS', 'GROCERY'),
    ('MS', 'FURNITURE'),
    ('PN', 'TOYS'),
    ('GH', 'FASHION'),
   
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()  
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='') 
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)  
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self): 
        return self.title
    
from django.db import models

class Customer(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50) 
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
   
    state = models.CharField(choices=STATE_CHOICES, max_length=100)   
    def __str__(self): 
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
