from datetime import date
import json

import pandas as pd
import requests
import logging

from pyopenmeteo.parameters.gps_position import GpsPosition
from pyopenmeteo.parameters.meteo_variable import MeteoVariable
from pyopenmeteo.queries.historical_data_query import HistoricalDataQuery

logger = logging.getLogger(__name__)


class HistoricalDataFetcher:

    endpoint_url = "https://archive-api.open-meteo.com/v1/archive"

    @classmethod
    def _get_response(cls, params: dict[str, str]):
        logger.debug(f"Running query to URL {cls.endpoint_url} with the following parameters: {params}")
        try:
            response = requests.get(url=cls.endpoint_url, params=params)
        except Exception as e:
            print(f"Caught the following exception: {e}")
        else:
            return response

    @staticmethod
    def _response_to_dataframe(response: requests.models.Response) -> pd.DataFrame:
        res = json.loads(response.text)
        return pd.DataFrame(data=res["hourly"])

    def get_data(self, position: GpsPosition, variable: MeteoVariable, start: date, end: date) -> pd.DataFrame:
        params = {
            "latitude": f"{position.latitude:.2f}",
            "longitude": f"{position.longitude:.2f}",
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": end.strftime("%Y-%m-%d"),
            "hourly": variable.value
        }
        response = self._get_response(params=params)
        if not response.ok:
            logger.warning(f"Response NOT OK inside {self.get_data.__name__}!")
        return self._response_to_dataframe(response=response)

    def run_query(self, query: HistoricalDataQuery):
        return self.get_data(
            position=query.gps_position,
            variable=query.meteo_variable,
            start=query.dates_interval.start,
            end=query.dates_interval.end
        )
