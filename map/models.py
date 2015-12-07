from django.db import models

# Create your models here.
class station(models.Model):
    sno = models.CharField(max_length=4)
    sna = models.CharField(max_length=128)
    sarea = models.CharField(max_length=128)
    lat = models.FloatField()
    lng = models.FloatField()
    ar = models.CharField(max_length=128)
    sareaen = models.CharField(max_length=256)
    snaen = models.CharField(max_length=256)
    aren = models.CharField(max_length=256)
    def __str__(self):
        return self.sno

class info(models.Model):
    sno = models.CharField(max_length=4)
    tot = models.PositiveSmallIntegerField()
    sbi = models.PositiveSmallIntegerField()
    mday = models.DateTimeField()
    bemp = models.PositiveSmallIntegerField()
    act = models.BooleanField()
    def __str__(self):
        return self.sno
