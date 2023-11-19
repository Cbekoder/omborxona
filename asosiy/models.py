from django.db import models
from accounts.models import Ombor

class  Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    olchov = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    miqdor = models.PositiveSmallIntegerField()
    kelgan_sana = models.DateField(null = True, blank = True)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom}, {self.brend}'
