import os
import random
from django.db import models

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


def upload_image_path(instance, filename):
	print("HAAAAAAALLO")
	print(instance)
	print(filename)
	new_filename = random.randint(1,3910209321)
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	print(final_filename)
	return f'demo/{new_filename}/{final_filename}'


class SlideshowSlide(models.Model):
	title 			= models.CharField(max_length=120)
	image 			= models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	@property
	def name(self):
		return self.title
