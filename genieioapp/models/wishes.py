from django.db import models
from .categories import Categories
from .locations import Locations
from .wisher import Wisher

class Wishes(models.Model):
    wisher = models.ForeignKey('Wisher', on_delete=models.DO_NOTHING, null=True)
    wish_body = models.CharField(max_length=55)
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING)
    location = models.ForeignKey('Locations', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    class Meta:
        verbose_name = ("Wish")
        verbose_name_plural = ("Wishes")

    