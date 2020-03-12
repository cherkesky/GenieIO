from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.expressions import F

class Wisher(models.Model):
    '''docstring'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=25, null=True)
    cid = models.IntegerField(max_length=11, null=True)

    # first_name, last_name, email, created_at, and is_active is all inherited from Django's user

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = (F('id').asc(nulls_last=True),)
        #Instances of F() act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.
        
        #In this case, order by the date the user joined (by ascending) and null fields last.