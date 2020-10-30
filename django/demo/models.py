from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    publishe_date = models.DateField(default=None, blank=True, null=True)
    cover = models.ImageField(upload_to='cover/')
    is_publised = models.BooleanField(default=False, blank=True, null=True)

