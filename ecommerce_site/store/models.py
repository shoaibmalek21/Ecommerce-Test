from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return '%s' % (self.name)

class SubCategory(models.Model):
	name = models.CharField(max_length=200, null=True)
	category = models.OneToOneField(Category,on_delete=models.CASCADE,primary_key=True)


	def __str__(self):
		return '%s' % (self.name)


class Product(models.Model):
	# SEL_ID = models.IntegerField()
	# PRO_ID = models.IntegerField()
	name = models.CharField(max_length=200, null=True)
	# category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)
	price = models.FloatField()
	# category = models.OneToOneField(Category,on_delete=models.CASCADE)
	# subcategory = models.OneToOneField(SubCategory,on_delete=models.CASCADE)

	def __str__(self):
		return '%s' % (self.name)


	def get_absolute_url(self):
	    return reverse('product-detail', kwargs={'pk':self.pk})

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = "images/placeholder.jpg"
		return url 


