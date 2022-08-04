from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
	avatar = models.ImageField(upload_to='images/users/', null=True, blank=True)
	is_online = models.BooleanField(default=False)
	age = models.PositiveIntegerField(null=True)

	def __str__(self):
		return self.username