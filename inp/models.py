from django.db import models


class Input(models.Model):
    name = models.CharField(max_length=20, default='')
    data = models.JSONField()
