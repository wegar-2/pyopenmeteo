import logging
from datetime import date

import coloredlogs

from pyom.fetchers.historical_data_fetcher import HistoricalDataFetcher
from pyom.parameters.gps_position import GpsPosition
from pyom.parameters.meteo_variable import MeteoVariable


def main():
    hdf = HistoricalDataFetcher()

    warsaw = GpsPosition(latitude=52.23, longitude=21.01)

    coloredlogs.set_level(logging.DEBUG)
    df = hdf.get_data(
        position=warsaw,
        variable=MeteoVariable.temperature2m,
        start=date(2023, 4, 1),
        end=date(2023, 4, 30)
    )
    coloredlogs.set_level(logging.INFO)
    print(df.head())
    print(df.tail())


if __name__ == "__main__":
    main()
