""" Serializers for planets app. """
from rest_framework import serializers
from .models import Planet, Terrain, Climate


class CreatePlanetSerializer(serializers.ModelSerializer):
    """ Serializer for Planet model. """
    terrains = serializers.PrimaryKeyRelatedField(queryset=Terrain.objects.all(), many=True)
    climates = serializers.PrimaryKeyRelatedField(queryset=Climate.objects.all(), many=True)

    class Meta:
        model = Planet
        fields = '__all__'


class PlanetSerializer(serializers.ModelSerializer):
    """ Serializer for Planet model. """
    terrains = serializers.StringRelatedField(many=True)
    climates = serializers.StringRelatedField(many=True)

    class Meta:
        model = Planet
        fields = '__all__'


class TerrainSerializer(serializers.ModelSerializer):
    """ Serializer for Terrain model. """
    class Meta:
        model = Terrain
        fields = '__all__'


class ClimateSerializer(serializers.ModelSerializer):
    """ Serializer for Climate model. """
    class Meta:
        model = Climate
        fields = '__all__'

