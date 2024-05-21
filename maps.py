import requests
from geopy.geocoders import Nominatim

def obter_coordenadas_por_rua(nome_rua):
    geolocator = Nominatim(user_agent="localidades_app");
    location = geolocator.geocode(nome_rua, language="pt-BR");

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

# Solicita o nome da rua ao usuário
nome_rua = input("Digite o nome da rua que deseja encontrar: ")
latitude, longitude = obter_coordenadas_por_rua(nome_rua)

if latitude and longitude:
    print(f"Latitude: {latitude}");
    print(f"Longitude: {longitude}");
else:
    print("Desculpe, não foi possivel encontrar sua localização");