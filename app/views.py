import requests
from django.shortcuts import render
from .models import Efemeride

def obtener_efemerides(request):
    year = 2024
    country_code = "CL"

    # Eliminar todas las efemérides existentes
    Efemeride.objects.all().delete()

    url = f'https://date.nager.at/api/v2/PublicHolidays/{year}/{country_code}'
    response = requests.get(url)
    efemerides_data = response.json()

    for efemeride in efemerides_data:
        fecha = efemeride['date']
        descripcion = efemeride['localName']
        Efemeride.objects.get_or_create(fecha=fecha, descripcion=descripcion)

    efemerides = Efemeride.objects.all()
    return render(request, 'calendario.html', {'efemerides': efemerides})
