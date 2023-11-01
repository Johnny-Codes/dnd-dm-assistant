import requests as r

base_url = "https://www.dnd5eapi.co"


def get_equipment_from_api():
    url = "/api/equipment-categories"
    response = r.get(base_url + url)
    return response.json()


def get_weapons_from_api():
    url = "/api/equipment-categories"
    response = r.get(base_url + url)
    return response.json()
