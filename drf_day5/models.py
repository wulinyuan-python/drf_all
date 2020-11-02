from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User5(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "bz_user5"
        verbose_name = "用户5"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
