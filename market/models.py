from django.contrib.auth.models import User
from django.db import models


class Productimage(models.Model):
    image = models.ImageField('Image:', upload_to='product_image/')


class Product(models.Model):
    name = models.CharField(verbose_name='Name:', blank=True, max_length=25)
    description1 = models.CharField(verbose_name='Description1:', max_length=50)
    description2 = models.TextField(verbose_name='Description2:')
    price = models.FloatField(verbose_name='Price:', blank=True)
    quantity = models.IntegerField(verbose_name='Quantity:', default=0)
    image = models.ForeignKey(Productimage, on_delete=models.CASCADE, verbose_name='Images:')


class Rating(models.Model):
     ball = models.IntegerField(verbose_name='Rate:')
     url_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
     url_to_prod = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    url_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    url_to_prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField('Text:')


class Editor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.TextField('Biography:')
