from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.PositiveBigIntegerField()
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
