from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email')
        # Normalize the address by lowercasing the domain
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)  # Hashes the password before storing it in the database
        user.save(using=self._db)  # Saves the object to the database using our custom manager
        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new super"""
        user =  self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
                      settings.AUTH_USER_MODEL,
                      on_delete=models.CASCADE
                   )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    # ManyToManyField used for relationships where an item can belong to many groups

    def __str__(self):
        """Returns the model as string representation"""
        return self.status_text