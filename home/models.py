from django.db.models import CharField
from django.db.models import TextField
from django.db.models import ImageField

from django.db import models as models

class Barang(models.Model) :
    foto = models.ImageField(upload_to = "media")
    nama = models.CharField(max_length = 100)
    harga = models.CharField(max_length = 25)

    def __str__(self) :
        return self.nama

