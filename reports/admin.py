from django.contrib import admin
from .models import Retailer, Service_Order, Distributor, Report

# Register your models here.
admin.site.register(Retailer)
admin.site.register(Service_Order)
admin.site.register(Distributor)
admin.site.register(Report)
