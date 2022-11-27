from django.db import models
from django.db import models
from django.urls import reverse

class Pc(models.Model):
    number = models.CharField(max_length=50)
    teh_sost =