# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Users(models.Model):
    # Specify if user is blocked or not.
    blocked = models.BooleanField(default=False)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_role = models.CharField(max_length=32, default='Users')


class Product(models.Model):
    product_id = models.IntegerField()              # Product ID
    # When does the product stop supporting.
    support_end_day = models.DateField()
    product_name = models.TextField(max_length=128)


class Bugs(models.Model):
    bug_id = models.IntegerField()                  # Bug ID.
    # Severity of the bug. 0 is the most severe, 3 is the least severe.
    severity = models.IntegerField()
    # Specify if it's visible for public.
    status = models.IntegerField()                  # Status of the bug.
    reported_by = models.IntegerField()             # Reported by which user.
    hide_to_public = models.BooleanField(default=False)
    information = models.TextField(max_length=65535)
    description = models.TextField(max_length=65535)


class BugStatus(models.Model):
    # Number of bug status.
    bug_status_id = models.IntegerField()
    # Name of bug status.
    bug_status_name = models.CharField(max_length=32)
    # Description of bug status.
    bug_status_description = models.CharField(max_length=256)


class BugSubscription(models.Model):
    bug_id = models.IntegerField()                  # Bug ID.
    # User ID who subscribe the bug.
    user_id = models.IntegerField()
