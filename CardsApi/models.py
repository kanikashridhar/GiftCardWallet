from django.db import models
from djmoney.models.fields import MoneyField
from django.conf import settings

#Details of the Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Card(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.PROTECT)
    VoucherNum = models.CharField(max_length=50)
    CardPin = models.CharField(max_length=50)
    CardValue = MoneyField(decimal_places=3,default=0,default_currency='AUD',max_digits=11 )
    IsArchived = models.BooleanField(default=False)

    class Meta:
        unique_together = ('Product', 'VoucherNum')





