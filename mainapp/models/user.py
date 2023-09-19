from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Должен быть задан логин')
        if email is None:
            raise TypeError('Должен быть задан email')
        if password is None:
            raise TypeError('Должен быть задан пароль')
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class BaseUser(AbstractBaseUser, PermissionsMixin):
    # связка логин пароль
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.CharField(verbose_name="email", max_length=40, default="", unique=True)
    
    last_name = models.CharField(verbose_name="фамилия", max_length=40, default="")
    first_name = models.CharField(verbose_name="имя", max_length=40, default="")
    
    registration_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # указать возможные роли пользователя
    is_staff = models.BooleanField(default=False, verbose_name='есть ли доступ к системе')
    is_active = models.BooleanField(default=True, verbose_name='активен ли сейчас пользователь')
    is_superuser = models.BooleanField(default=False, verbose_name='администратор всей системы')
    is_manager = models.BooleanField(default=False, verbose_name='менеджер')
    is_constructor = models.BooleanField(default=False, verbose_name='проектировщик')
    is_checker = models.BooleanField(default=False, verbose_name='проверяющий')
    is_teh_control = models.BooleanField(default=False, verbose_name='тех контроль')
    is_teh_control = models.BooleanField(default=False, verbose_name='нормоконтроль')
    is_approver = models.BooleanField(default=False, verbose_name='утверждающий')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'