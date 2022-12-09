from django.db import models

class Location(models.Model):
    """Location model.

    A location represented by a title and a zipcode.
    """
    title = models.CharField("Title", max_length=150)
    zipcode = models.CharField("ZIP Code", max_length=5)

    def __str__(self):
        return self.title