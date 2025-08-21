from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,username,password=None):
        if not email:
            raise ValueError("user must have an email")
        
        if not username:
            raise ValueError("user must provide a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname
        )
        user.set_password(password)
        user.save(using =self._db)
        return user

    def create_superuser(self,email,firstname,lastname,username,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# The User Model been created for the project.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    profile_picture = models.ImageField(upload_to='media',blank=True, null= True)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
