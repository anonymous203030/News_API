from django.db import models

from django.contrib.auth.models import AbstractBaseUser,  BaseUserManager, PermissionsMixin


class UserManage(BaseUserManager):
    def create_user(self, username, email, is_upgraded, password=None,):

        if username is None:
            raise TypeError('users should have an username')
        if email is None:
            raise TypeError('users should have an email')

        user = self.model(username=username, email=self.normalize_email(email), is_upgraded=is_upgraded)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, email, is_upgraded, password):
        if password is None:
            raise TypeError('Password should not to be none.')

        user = self.create_user(username, email,is_upgraded, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=50, unique=True, db_index=True)
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_upgraded = models.BooleanField(default=False) #For Payment System
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_upgraded']

    objects = UserManage()

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    image = models.FileField(upload_to='profile_img/', blank=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField()
    birthday = models.DateField(auto_now_add=False)
    gender = models.CharField(choices=GENDER, max_length=100, )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{User.username}:{self.first_name} {self.last_name}'

