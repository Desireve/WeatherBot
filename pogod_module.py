from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from torch_optimizer import get
from config import POGODA_TOKEN
 
owm = OWM(POGODA_TOKEN)
mgr = owm.weather_manager()


def get_pogoda(gorod_name):
    observa = mgr.weather_at_place(gorod_name + ',RU')
    weather1 = observa.weather
    temp = weather1.temperature('celsius')

    return temp


