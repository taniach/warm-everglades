from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	icon = models.ImageField(upload_to = 'images/')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Product(models.Model):
	description = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	icon = models.ImageField(upload_to = 'images/')
	categoryID = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	lowLimit = models.IntegerField("quantity below which alert is shown for low stock", default=20)

	def __str__(self):
		return self.description