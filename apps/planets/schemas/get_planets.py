from typing import List, Optional, Any
from pydantic import BaseModel


class Planet(BaseModel):
    name: str
    population: Optional[Any]
    terrains: List[str]
    climates: List[str]


class GroupPlanets(BaseModel):
    planets: List[Planet]


class AllPlanetsData(BaseModel):
    allPlanets: GroupPlanets


class PlanetsResponse(BaseModel):
    data: AllPlanetsData
