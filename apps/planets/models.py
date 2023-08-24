from django.db import models
from apps.core.models import GenericModel


class Planet(GenericModel):
    name = models.CharField(max_length=255, unique=True)
    population = models.BigIntegerField(blank=True, null=True)
    terrains = models.ManyToManyField('Terrain', through='PlanetTerrains', related_name='planets')
    climates = models.ManyToManyField('Climate', through='PlanetClimates', related_name='planets')

    def __str__(self):
        return self.name


class PlanetTerrains(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    terrain = models.ForeignKey('Terrain', on_delete=models.CASCADE)


class PlanetClimates(models.Model):
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    climate = models.ForeignKey('Climate', on_delete=models.CASCADE)


class Terrain(GenericModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Climate(GenericModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
