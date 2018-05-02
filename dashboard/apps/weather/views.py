from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm

def weather(request):

    # URL to Open Weather Map API
    # q = {} : placeholder for cityname
    # units=metric : temperature unit is Celcius
    # appid=45c3028b83d45e07f00213485024bed4 : API Key from personal account at Open Weather Map
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=45c3028b83d45e07f00213485024bed4'

    if request.POST.get('name'):
        # using the data of the userinput (within the post request)
        city_form = CityForm(request.POST)
        print(request.POST)

        # validates and saves input to the database
        city_form.save()


    # to have a clear input field again after adding another city
    city_form = CityForm()

    # fetch all City objects from the database
    cities = City.objects.all()

    # list to store all weather data per city
    city_list = []

    for city in cities:

        resp = requests.get(url.format(city)).json()


        weather_context = {
            'city': resp['name'],
            'temperature': resp['main']['temp'],
            'temp_unit': '° C',
            'description': resp['weather'][0]['description'],
            'icon': resp['weather'][0]['icon'],
        }

        print(weather_context)
        city_list.append(weather_context)

    print(city_list)
    context = {'weather_category': 'Weather', 'city_list': city_list, 'city_form': city_form}

    return context
    #return render(request, 'index.html', context)


