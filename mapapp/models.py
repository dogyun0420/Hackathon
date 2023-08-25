from django.db import models

class OutdoorShelter(models.Model):
    vt_acmdfclty_nm = models.CharField(max_length=255)
    dtl_adres = models.CharField(max_length=255)
    xcord = models.FloatField()
    ycord = models.FloatField()

    def __str__(self):
        return self.vt_acmdfclty_nm