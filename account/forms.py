from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = Account
		fields = UserCreationForm.Meta.fields + ('email', 'age',)


class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = Account
		fields = UserChangeForm.Meta.fields