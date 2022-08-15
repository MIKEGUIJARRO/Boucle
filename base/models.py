from django.db import models
from django.conf import settings
from .choices import CATEGORY_CHOICES, STAGE_CHOICES


class Cloth(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=3)
    stage = models.IntegerField(choices=STAGE_CHOICES, default=1)
    drop_off_date = models.DateField(null=True)
    pick_up_date = models.DateField(null=True)
    pick_up_hour = models.TimeField(null=True)

    def __str__(self):
        return self.name
