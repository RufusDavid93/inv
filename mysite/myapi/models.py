from django.db import models
from django.db.models import DateField
from django.utils import timezone

mouse_assigned = [
    ('Y', 'YES'),
    ('N', 'NO'),
]

device_assigned = [
    ('L', 'Laptop'),
    ('D', 'Desktop'),
]

slack_id = [
    ('Y', 'YES'),
    ('N', 'NO'),
]

adobe_id = [
    ('Y', 'YES'),
    ('N', 'NO'),
]

office_tools = [
    ('MS', 'MS_OFFICE'),
    ('W', 'WPS'),
    ('N', 'NO'),
]

device_assigned_by = [
    ('R', 'Rufus'),
    ('N', 'Nikhil'),
]

gmail_id = [
    ('Y', 'YES'),
    ('N', 'NO'),

]


class Lowerparel(models.Model):
    new_joinee = models.CharField(max_length=60)
    designation = models.CharField(max_length=60, null=True)
    current_ou = models.CharField(max_length=60)
    date_of_joinee = models.DateField(default=timezone.now)
    current_ou_removed = models.CharField(max_length=60)
    device_assigned = models.CharField(max_length=1, choices=device_assigned)
    mouse_assigned = models.CharField(max_length=1, choices=mouse_assigned)
    slack_id = models.CharField(max_length=1, choices=slack_id)
    adobe_id = models.CharField(max_length=1, choices=adobe_id)
    gmail_id = models.CharField(max_length=1, choices=gmail_id)
    office_tools = models.CharField(max_length=3, choices=office_tools)
    device_assigned_by = models.CharField(max_length=1, choices=device_assigned_by)

    def __str__(self):
        return self.new_joinee


class Bhiwandi(models.Model):
    new_joinee = models.CharField(max_length=60)
    designation = models.CharField(max_length=60, null=True)
    date_of_joinee = models.DateField(default=timezone.now)
    current_ou_removed = models.CharField(max_length=60)
    device_assigned = models.CharField(max_length=1, choices=device_assigned)
    mouse_assigned = models.CharField(max_length=1, choices=mouse_assigned)
    slack_id = models.CharField(max_length=1, choices=slack_id)
    adobe_id = models.CharField(max_length=1, choices=adobe_id)
    gmail_id = models.CharField(max_length=1, choices=gmail_id)
    office_tools = models.CharField(max_length=3, choices=office_tools)
    device_assigned_by = models.CharField(max_length=1, choices=device_assigned_by)

    def __str__(self):
        return self.new_joinee


class STORE(models.Model):
    new_joinee = models.CharField(max_length=60)
    date_of_joinee = models.DateField(default=timezone.now)
    mouse_assigned = models.CharField(max_length=1, choices=mouse_assigned)
    device_assigned_by = models.CharField(max_length=1, choices=device_assigned_by)

    def __str__(self):
        return self.new_joinee


class V_TECH(models.Model):
    device_ordered = models.CharField(max_length=100)
    quantity = models.CharField(max_length=3)
    purchase_order_id = models.CharField(max_length=5)
    delivery_date = models.DateField(default=timezone.now)

    device_arrived = models.CharField(max_length=100)
    bill_id = models.CharField(max_length=5)
    delivered_quantity = models.CharField(max_length=3)
    received_by = models.CharField(max_length=10)

    device_return = models.CharField(max_length=100)
    date: DateField = models.DateField(default=timezone.now)

    def __str__(self):
        return self.device_ordered