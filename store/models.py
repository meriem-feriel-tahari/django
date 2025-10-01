from django.db import models

# Create your models here.
class Collection(models.Model):
    title=models.CharField(max_length=255)
    
class product(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)#this two arguments are required
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection,)
    # chaque collection has multiple proucts
    # so it is like one to many relationship one collection has many products 
    
class Customer(models.Model):
    # this sku is going to be created in case i want the sku filed to be the id 
    # sku=models.CharField(max_length=10,primary_key=True)
    Bronze="B",
    Silver="S",
    Gold="G",
    membership_CHOICES=[
        (Bronze,"Bronze"),
        (Silver,"Silver"),
        (Gold,"Gold")
    ]
    first_name=models.CharField(max_length=250) 
    last_name=models.CharField(max_length=250)
    email= models.EmailField(unique=True)
    phone=models.CharField(max_length=250)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=membership_CHOICES,default='B')
class order(models.Model):
    Placed_At=models.DateTimeField(auto_now_add=True)
    Pending="P",
    Complete="C",
    Failed="F",
    Choices=[
        (Pending,"Pending"),
        (Complete,"Complete"),
        (Failed,"Failed"),
             ],
    payment_status=models.CharField(max_length=1,choices=Choices,default=Pending)
    # customer=models.ForeignKey(Customer,on_delete=models.CASCADE,primary_key=True)  

class adress(models.Model):
    street=models.CharField(max_length=20)    
    city=models.CharField(max_length=20)  
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)  
    # this on delet arguments tell that if the customer is deleted all its orders are deleted 
    # and the primary key tells that this is going to be considered as the primary key
    
    