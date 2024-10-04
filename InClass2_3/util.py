"""Module providing a function printing python version."""
from datetime import datetime
# py -m pip install --upgrade pip
# py -m pip install python-dateutil
from dateutil.relativedelta import relativedelta

import constant
import math

def liquor_age(birthday): # [missing-function-docstring]
    """Function printing python version."""
    birthday = datetime.strptime(birthday, constant.DATE_FORMAT)
    delta = relativedelta(datetime.now(), birthday)

    return delta.years >= constant.LIQUOR_AGE

def degrees_radians(degrees):
  return degrees * constant.PI / 180

def dist_earth(lat1, lon1, lat2, lon2):
  dLat = degrees_radians(lat2-lat1)
  dLon = degrees_radians(lon2-lon1)

  lat1 = degrees_radians(lat1)
  lat2 = degrees_radians(lat2)

  a = math.sin(dLat/2) * math.sin(dLat/2) + \
          math.sin(dLon/2) * math.sin(dLon/2) * math.cos(lat1) * math.cos(lat2); 
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  return constant.EARTH_RADIUM_KM * c
