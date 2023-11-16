from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(verbose_name="name", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
