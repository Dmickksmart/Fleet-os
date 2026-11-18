from django.db import models
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=100)
    class Meta: app_label = "fleet"

class Vehicle(models.Model):
    registration = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="available")
    class Meta: app_label = "fleet"

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    license_number = models.CharField(max_length=30, unique=True)
    class Meta: app_label = "fleet"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default="reserved")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta: app_label = "fleet"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(max_length=20, default="cash")
    class Meta: app_label = "fleet"
