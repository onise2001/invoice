from django.db import models
import random, string
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

def gen_serial_num():
    return "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(random.choices(string.digits, k=4))


class Status(models.Model):
    name = models.CharField(max_length=100,unique=True)

    @classmethod
    def get_default(cls):
        name,created = cls.objects.get_or_create(
            name = "Pending"
        )
        return name
   



class Invoice(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateField(blank=True, null=True)
    paymentDue = models.DateField(blank=True, null=True)
    paymentTerms = models.IntegerField(blank=True, null=True)
    clientName = models.CharField(max_length=200, blank=True, null=True)
    clientEmail = models.EmailField(blank=True, null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE, default=Status.get_default)
    senderAddress = models.JSONField(blank=True,null=True)
    clientAddress = models.JSONField(blank=True,null=True)
    items = models.JSONField(blank=True,null=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    
