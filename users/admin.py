from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ParentUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group

from users.models import User


class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('email', )
	
	def clean_password2(self):
		"""
		Check that the two password entries match.
		"""
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match.")
		return password2
	
	def save(self, commit=True):
		"""
		Saves the password provided in hashed format.
		"""
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password2'])
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()
	
	class Meta:
		models = User
		fields = ('email', 'name', 'slug', 'password', 'is_active', 'is_admin')
	
	def clean_password(self):
		"""
		Required by Django.
		"""
		return self.initial['password']


class UserAdmin(ParentUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	list_display = ('email', 'slug', 'name', 'created', 'last_login', 'is_active', 'is_admin')
	list_filter = ('is_active', 'is_admin')
	fieldsets = (
		(None, {'fields': ('email', 'name', 'slug', 'password', 'is_active', 'is_admin')}),
	)
	add_fieldsets = (
		(None, {
			'fields': ('email', 'password', 'is_active', 'is_admin'),
			'classes': ('wide', )
		}),
	)
	search_fields = ('email', 'name', 'slug')
	ordering = ('email', 'name', 'slug', 'created', 'last_login')
	filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

