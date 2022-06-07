from django.db import models


class GuestModel(models.Model):
    fullname = models.CharField(max_length=300)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return f'Name: {self.fullname}'

    class Meta:
        verbose_name = 'guest'
        verbose_name_plural = 'guests'
