from enum import Enum


class MeteoVariable(Enum):
    temperature2m = "temperature_2m"
    surface_pressure = "surface_pressure"
    sea_level_pressure = "pressure_msl"
    total_precipitation = "precipitation"
    rain = "rain"
    snow = "snow"
