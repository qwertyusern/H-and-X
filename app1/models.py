from django.db import models

class Togri(models.Model):
    soz=models.CharField(max_length=30)
    def __str__(self):
        return self.soz
class Notogri(models.Model):
    hatosoz=models.CharField(max_length=30)
    togri=models.ForeignKey(Togri,on_delete=models.CASCADE)
    def __str__(self):
        return self.hatosoz
