from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	icon = models.ImageField(upload_to = 'static/images/')

	def __str__(self):
		return self.name

class Product(models.Model):
	description = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	icon = models.ImageField(upload_to = 'static/images/')
	categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.description

class Transaction(models.Model):
	date = models.DateField()
	quantity = models.IntegerField(default=0)
	description = models.CharField(max_length=200)
	BUY = 'BUY'
	USE = 'USE'
	TRANSACTION_CHOICES = (
		(BUY, 'Buy from supplier'),
		(USE, 'Use for customer'),
	)

	transactionType = models.CharField(
		max_length=3,
		choices=TRANSACTION_CHOICES,
		default=USE,
	)

	productID = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.description
		
		