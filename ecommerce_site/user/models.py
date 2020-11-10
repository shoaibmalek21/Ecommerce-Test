# from django.db import models
# from django.contrib.auth.models import User

# class Customer(models.Model):
# 	SELLER_ID = models.IntegerField()
# 	first_name = models.CharField(max_length=30, help_text='Optional.')
# 	last_name = models.CharField(max_length=30, help_text='Optional.')
# 	address = models.CharField(max_length=30)
# 	email = models.EmailField(max_length=50)
# 	contact = models.IntegerField()
# 	city = models.CharField(max_length=20)

# 	def __str__(self):
# 		return "Customer {} - {}".format(self.id, self.first_name)	

# 	