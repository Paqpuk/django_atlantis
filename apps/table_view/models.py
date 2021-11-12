from django.db import models


class HILs(models.Model):

    name = models.CharField(max_length=1000, verbose_name="hostname")
    station = models.CharField(max_length=10, verbose_name="station")
    responsible = models.CharField(max_length=10, verbose_name="responsible name")




