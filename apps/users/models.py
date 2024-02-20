from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from utils.validates.validates import validate_digits,validate_alnum,validate_letters_and_spaces,validate_letters_numbers_and_spaces


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    
    def create_user(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, True , False ,**extra_fields)
    
    def create_superuser(self, username, email, password = None, **extra_fields):
        return self._create_user(username, email, password, True , True ,**extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):   
    username = models.CharField('Username',validators=[MinLengthValidator(3),validate_alnum],max_length=50, unique=True,blank = False, null= False)
    email = models.EmailField('Email', max_length=50 , unique=True, blank = False, null= False)
    movil =models.CharField('Movil',validators=[MinLengthValidator(8),validate_digits], max_length=8, blank = False, null= False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    name = models.CharField('Nombre', max_length=50,validators=[MinLengthValidator(3),validate_letters_and_spaces],blank=False, null=False)
    last_name = models.CharField('Apellidos',validators=[MinLengthValidator(3),validate_letters_and_spaces], max_length=50, blank=False, null=False)
    ci=models.CharField('Carnet',validators=[MinLengthValidator(11),validate_digits], max_length=11, unique=False ,blank = False, null= False)
    
    class Meta:    
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'movil','name','last_name','ci',]
    
    def natural_key(self):
        return (self.username)
    
    def __str__(self) -> str:
        return f'{self.username}'