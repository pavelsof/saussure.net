from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
		Creates and saves a user.
		"""
		if not email:
			raise ValueError("Users must have an email address.")
		user = self.model(
			email = self.normalize_email(email)
		)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_superuser(self, email, password):
		"""
		Creates and saves a super user.
		"""
		user = self.create_user(email, password)
		user.is_admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(max_length=240, unique=True)
	name = models.CharField(max_length=240, default="Anon")
	slug = models.SlugField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	
	objects = UserManager()
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	
	@property
	def is_staff(self):
		"""
		Mimicks the is_staff property.
		"""
		return self.is_admin
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.email
	
	def get_full_name(self):
		"""
		Returns the user's full name. Required by Django.
		"""
		return self.email
	
	def get_short_name(self):
		"""
		Returns the user's short name. Required by Django.
		"""
		return self.email
	
	def has_module_perms(self, app_label):
		"""
		Whether the user can view the app specified.
		"""
		return True
	
	def has_perm(self, perm, obj=None):
		"""
		Whether the user has the permission specified.
		"""
		return True

