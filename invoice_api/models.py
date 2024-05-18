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
    description = models.TextField()
    createdAt = models.DateField()
    paymentDue = models.DateField()
    paymentTerms = models.IntegerField()
    clientName = models.CharField(max_length=200)
    clientEmail = models.EmailField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE, default=Status.get_default)
    senderAddress = models.JSONField()
    clientAddress = models.JSONField()
    items = models.JSONField()
    total = models.DecimalField(max_digits=20, decimal_places=2)
    
