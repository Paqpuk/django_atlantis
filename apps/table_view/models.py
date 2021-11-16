from django.db import models
from django.core.exceptions import ValidationError
import re


def simx_validator(inp):
    if re.match(r'^simx\d+$', inp):
        return True
    else:
        raise ValidationError(f"Please provide a standard name. Ex: 'simx15'")


class HILs(models.Model):

    name = models.CharField(max_length=1000, verbose_name="hostname", validators=[simx_validator])
    station = models.CharField(max_length=10, verbose_name="station")
    responsible = models.CharField(max_length=10, verbose_name="responsible name")



