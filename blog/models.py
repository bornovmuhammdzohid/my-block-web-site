from django.db import models
from django.conf import settings
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, last_name, password=None):
        if not email or not username or not last_name:
            raise ValueError('bosh qatorlar bor')
        if password is None or len(password) < 5:
            raise ValueError('parol notogri')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, last_name, password=None):
        user = self.create_user(
            email,
            username=username,
            last_name=last_name,
            password=password
        )
        user.is_admin = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=100, unique=True, null=True)
    last_name = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name']

    def __str__(self):
        return "{}- {}".format(self.username, self.last_name)
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin