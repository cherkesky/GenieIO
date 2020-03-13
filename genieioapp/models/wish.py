from django.db import models
from .category import Category
from .location import Location
from .wisher import Wisher

class Wish(models.Model):
    wisher = models.ForeignKey('Wisher', on_delete=models.DO_NOTHING, null=True)
    wish_body = models.CharField(max_length=55)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    

    class Meta:
        verbose_name = ("Wish")
        verbose_name_plural = ("Wishes")

    