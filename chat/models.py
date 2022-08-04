from django.db import models
from account.models import Account

# Create your models here.

class Chat(models.Model):
	title = models.CharField(max_length=50, null=True, blank=True)
	avatar = models.ImageField(upload_to='images/chat/', null=True, blank=True)

	members = models.ManyToManyField(Account, related_name="chat", blank=True)
	muted = models.ManyToManyField(Account, related_name='user_muted', blank=True)
	pinned = models.ManyToManyField(Account, related_name='user_pinned', blank=True)
	archived = models.ManyToManyField(Account, related_name='user_archived', blank=True)
	is_group = models.BooleanField(default=False)

	def __str__(self):
		if self.title:
			return self.title
		else:
			return str(self.id)


class Message(models.Model):
	from_user = models.ForeignKey(Account, on_delete=models.CASCADE)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', blank=True)
	text = models.TextField()
	file = models.FileField(upload_to='files/', null=True, blank=True)
	read = models.ManyToManyField(Account, related_name='user_read', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text[:50]