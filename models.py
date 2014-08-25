from django.db import models

# Create your models here.


class Dojo(models.Model):

    name = models.CharField(
        max_length=255,
    )

    address = models.CharField(
        max_length=255,
    )

    city = models.CharField(
        max_length=255,
    )

    state = models.CharField(
        max_length=12,
    )

    postal_code = models.CharField(
        max_length=14,
    )

    ryu = models.CharField(
        max_length=64,
    )

    website = models.URLField() 

    email = models.EmailField() 

    def __str__(self):
      return self.name