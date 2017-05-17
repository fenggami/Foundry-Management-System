# from django.db import models
# from django.contrib.auth.models import User
# # Create your models here.
#
#
# class Machine(models.Model):
#     bianhao = models.CharField(max_length=50)
#     type = models.CharField(max_length=30)
#     responsor = models.ForeignKey(User, null=False,blank=False)
#     buy_time = models.DateTimeField(auto_now_add=True)
#
#
# class Order(models.Model):
#     bianhao = models.CharField(max_length=50)
#     in_time = models.DateTimeField(auto_now_add=True)
#     order_info = models.CharField(max_length=200)
#     product = models.ForeignKey(Product)
#
#
# class Product(models.Model):
#     fullname = models.CharField(max_length=50)
#     daihao = models.CharField(max_length=50)
#     amount = models.IntegerField(default=0)
#     des = models.CharField(max_length=200)
#
#
# class Raw_material(models.Model):
#     daihao = models.CharField(max_length=50)
#     name = models.CharField(max_length=50)
#     amount = models.IntegerField(default=0)
#
#
#
#
#
#
#
#
#
#
