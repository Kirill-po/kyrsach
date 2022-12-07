from django.db import models
from django.db import models
from django.urls import reverse

class Pc(models.Model):
    price = models.IntegerField()
    type = models.TextField(max_length=20)
    Time_busy = models.TimeField(null=True, blank=True)
    busy = models.BooleanField()
    tech_ac = models.BooleanField()


class Clients(models.Model):
    FIO = models.TextField(max_length=120)
    email = models.TextField(max_length=60)
    number = models.IntegerField()
    password = models.TextField(max_length=60)

class Time_base(models.Model):
    PC_id = models.ForeignKey(

        Pc,
        on_delete=models.CASCADE,
    )
    price = models.ManyToManyField(Pc, verbose_name="цена", related_name="price_pc",)
    Time_busy = models.ManyToManyField(

        Pc,
        verbose_name="время",
        related_name="time_bron",

    )
    FIO = models.ManyToManyField(
        Clients,
        verbose_name="имя",
        related_name="name_user",

    )
    number = models.ManyToManyField(

        Clients,
        verbose_name="номер",
        related_name="number_user",

    )
