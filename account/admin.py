from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Account
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = Account
	list_display = ('username', 'email', 'age', 'is_staff')
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('age',)}),
	)
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('age', 'avatar')}),
	)

admin.site.register(Account, CustomUserAdmin)