from rest_framework.viewsets import ModelViewSet
from .serializers import PlanetSerializer, TerrainSerializer, ClimateSerializer, CreatePlanetSerializer
from .models import Planet, Terrain, Climate, PlanetClimates, PlanetTerrains
from rest_framework.permissions import AllowAny
from apps.core.pagination import StandardResultsSetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from .services import get_planet_data
from rest_framework.response import Response
from rest_framework import status
from apps.planets.schemas.get_planets import PlanetsResponse


class PlanetViewSet(ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
    pagination_class = StandardResultsSetPagination
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ["terrains", "climates"]
    search_fields = ["name", "population"]
    ordering_fields = ["name", "created_at", "updated_at"]

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return CreatePlanetSerializer
        return PlanetSerializer


class TerrainViewSet(ModelViewSet):
    serializer_class = TerrainSerializer
    queryset = Terrain.objects.all()
    pagination_class = StandardResultsSetPagination
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name"]
    ordering_fields = ["name", "created_at", "updated_at"]


class ClimateViewSet(ModelViewSet):
    serializer_class = ClimateSerializer
    queryset = Climate.objects.all()
    pagination_class = StandardResultsSetPagination
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
    permission_classes = [AllowAny]
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ["name"]
    ordering_fields = ["name", "created_at", "updated_at"]


class GetPlanetsData(APIView):
    serializer_class = None
    def get(self, request):
        planet_data = get_planet_data()
        if planet_data:
            validation = PlanetsResponse(**planet_data)
            if validation:
                planets = validation.data.allPlanets.planets
                for planet in planets:
                    planet_obj, _ = Planet.objects.get_or_create(name=planet.name, population=planet.population)
                    terrains = planet.terrains
                    climates = planet.climates
                    for terrain in terrains:
                        terrain_obj, _ = Terrain.objects.get_or_create(name=terrain)
                        PlanetTerrains.objects.create(planet=planet_obj, terrain=terrain_obj)

                    for climate_name in climates:
                        climate_obj, _ = Climate.objects.get_or_create(name=climate_name)
                        PlanetClimates.objects.create(planet=planet_obj, climate=climate_obj)

                return Response({"message": "Planets populated successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Error populating planets"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Error populating planets"}, status=status.HTTP_400_BAD_REQUEST)
