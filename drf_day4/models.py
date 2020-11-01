from django.db import models


# Create your models here.

class Workers(models.Model):
    w_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'bz_workers'
        verbose_name = '工人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.w_name
