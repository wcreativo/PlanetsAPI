""" Config URLs. """
from rest_framework.routers import DefaultRouter
from rest_framework.urls import path

from apps.planets.views import PlanetViewSet, TerrainViewSet, ClimateViewSet, GetPlanetsData

APP_NAME = "planets"

router = DefaultRouter()
router.register(r"planets", PlanetViewSet, basename="planets")
router.register(r"terrains", TerrainViewSet, basename="terrains")
router.register(r"climates", ClimateViewSet, basename="climates")

urlpatterns = router.urls

urlpatterns += [
    path("get_planets_data/", GetPlanetsData.as_view(), name="get_planets_data"),
]