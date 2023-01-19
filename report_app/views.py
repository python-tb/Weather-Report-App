from django.shortcuts import render
import urllib
import json


def home(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        # MY api key of weather app.
        api_key = "adf3960c9232886fa73a5165abef766b"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        source = urllib.request.urlopen(url).read()
        # print(source,type(source))  # it return type bytes and json data to us.
        data = json.loads(source)

        context = {
            'temp': data['main']['temp'],
            'city': city_name,
            'icon': data['weather'][0]['icon'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],


        }

        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
