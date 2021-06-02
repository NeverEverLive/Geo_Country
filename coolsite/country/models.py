from django.contrib.gis.db import models


class Country(models.Model):
    name = models.CharField("Country", max_length=150,)
    location = models.MultiPolygonField(verbose_name="Coordinates")

    def __str__(self):
        return self.name
 
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField('City', max_length=150)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Image", upload_to='cities/')
    country = models.ForeignKey(
        "Country", on_delete=models.PROTECT
    )
    location = models.MultiPolygonField(verbose_name="Coordinates")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Capital(models.Model):
    name = models.CharField("Capital", max_length=100)
    country = models.OneToOneField(
        Country, verbose_name="Capital", on_delete=models.PROTECT
    )
    location = models.MultiPolygonField(verbose_name="Coordinates")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Capital"
