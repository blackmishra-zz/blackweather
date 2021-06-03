from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def home(request):
    if request.method == "POST":
        lon = request.POST["lon"]
        lat = request.POST["lat"]
        source = urllib.request.urlopen(
            "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat="
            + lon
            + "&lat="
            + lat
            + ""
        ).read()

        # convert  json file into python dectionary
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data["sys"]["country"]),
            "cor": str(list_of_data["coord"]["lon"])
            + " "
            + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]),
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "main": str(list_of_data["weather"][0]["main"]),
            "description": str(list_of_data["weather"][0]["description"]),
            "icon": list_of_data["weather"][0]["icon"],
        }
    else:
        data = {}
    return render(request, "weather/index.html", data)
