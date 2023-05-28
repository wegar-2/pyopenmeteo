from enum import Enum


class MeteoVariable(Enum):
    temperature2m = "temperature_2m"
    surface_pressure = "surface_pressure"
    total_precipitation = "precipitation"
    rain = "rain"
    snow = "snow"
