from django.db import models
import django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
# Create your models here.
class UserBase(AbstractBaseUser, PermissionsMixin):
