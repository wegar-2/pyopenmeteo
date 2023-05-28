from pyopenmeteo.parameters.gps_position import GpsPosition
from pyopenmeteo.parameters.meteo_variable import MeteoVariable
from pyopenmeteo.parameters.dates_interval import DatesInterval


class HistoricalDataQuery:
    gps_position: GpsPosition
    meteo_variable: MeteoVariable
    dates_interval: DatesInterval
