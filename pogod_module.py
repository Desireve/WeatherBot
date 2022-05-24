from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from config import POGODA_TOKEN
 
owm = OWM(POGODA_TOKEN)
mgr = owm.weather_manager()


def get_temp(gorod_name):
    observa = mgr.weather_at_place(gorod_name + ',RU')
    weather1 = observa.weather
    temp = weather1.temperature('celsius')

    return temp

def get_osadki_status(gorod_name):
    observa = mgr.weather_at_place(gorod_name + ',RU')
    weather1 = observa.weather
    rain = weather1.detailed_status

    return rain

def get_wind_speed(gorod_name):
    observa = mgr.weather_at_place(gorod_name + ',RU')
    weather1 = observa.weather.wind()

    windspeed  = weather1.get('speed')

    return windspeed




