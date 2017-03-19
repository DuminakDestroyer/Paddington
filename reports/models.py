from django.db import models
from django.utils import timezone

class Retailer(models.Model):
    retailer_file = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/retailers')
    upload_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.retailer_file + str(self.upload_date)


class Service_Order(models.Model):
    so_file = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/service_orders')
    upload_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.so_file + str(self.upload_date)


class Distributor(models.Model):
    distributor = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/distributors')
    upload_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.distributor + str(self.upload_date)

class Report(models.Model):
    report = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/distributors')
    upload_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.report + str(self.upload_date)