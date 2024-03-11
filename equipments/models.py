from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):# ميثود عشان تعرض لنا النيمز في الادمن بانل
        return self.name

class ItemDetails(models.Model):
    price=models.FloatField()
    desc=models.CharField(max_length=1000,null=True)
    weight=models.FloatField(null=True)
    color=models.CharField(max_length=50, null=True)
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150,null=True)
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)

class Cart(models.Model):
    id_product=models.IntegerField()
    id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    image=models.CharField(max_length=150,null=True)
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField(null=True)
    status=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)