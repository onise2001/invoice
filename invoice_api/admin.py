from django.contrib import admin
from .models import  Invoice,Status
# Register your models here.


admin.site.register(Status)
admin.site.register(Invoice)