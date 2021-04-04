from django.db import models

class Pizza(models.Model):
	"""A entered kind of pizza"""
	name = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.name

class Topping(models.Model):
	"""A entered kind of pizza"""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'toppings'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.name) >= 50:
			return f"{self.name[:50]}..."
		else:
			return self.name
