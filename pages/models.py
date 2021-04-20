from django.db import models

class Files(models.Model):
	diety_name = models.CharField(max_length=200)
	diety_image = models.CharField(max_length=200)
	file_name = models.CharField(max_length=200)
	file_size = models.CharField(max_length=200)

	def __str__(self):
		return self.diety_name