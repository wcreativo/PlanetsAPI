from rest_framework.response import Response
from rest_framework import status
import requests


def get_planet_data():
    """Get planet data from SWAPI GraphQL API"""
    endpoint = "https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20%7BallPlanets%7Bplanets%7Bname%20population%20terrains%20climates%7D%7D%7D"
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(e)
        return None




