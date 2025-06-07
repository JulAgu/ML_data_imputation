import os
from datetime import date
import pandas as pd
import openmeteo_requests
from openmeteo_sdk.Variable import Variable
"""
This script contains a modular pipeline to request data from the Open-Meteo historic API.
#TODO: As we're doing punctual requests, I'm not going to implement a cache system or a retry system for now.
"""

API_URL = "https://archive-api.open-meteo.com/v1/archive"
REQUESTED_VARS = ["weather_code",
                  "temperature_2m_mean",
                  "temperature_2m_max",
                  "temperature_2m_min",
                  "precipitation_sum",
                  "rain_sum",
                  "precipitation_hours",
                  "daylight_duration",
                  "wind_speed_10m_max",
                  "wind_gusts_10m_max",
                  "shortwave_radiation_sum",
                  "et0_fao_evapotranspiration",
                  ]


def request_om_data(longitudes, latitudes, start_date, end_date):
    if len(latitudes) != len(longitudes):
        raise ValueError("The number of latitudes and longitudes must be the same.")
    om = openmeteo_requests.Client()
    params = {
        "latitude": latitudes,
        "longitude": longitudes,
        "start_date": start_date,  # Date format should be "YYYY-MM-DD"
        "end_date": end_date,
        "daily": REQUESTED_VARS,
    }
    responses = om.weather_api(API_URL, params=params)
    return responses


def om_response_to_df(response):
    daily_response = response.Daily()
    daily_dico = dict()
    for index, name in enumerate(REQUESTED_VARS):
        daily_dico[name] = daily_response.Variables(index).ValuesAsNumpy()
    daily_dico["date"] = pd.date_range(start = pd.to_datetime(daily_response.Time(), unit = "s", utc = True),
                                       end = pd.to_datetime(daily_response.TimeEnd(), unit = "s", utc = True),
                                       freq = pd.Timedelta(seconds = daily_response.Interval()),
                                       inclusive = "left"
                                       )
    daily_dico["latitude"] = response.Latitude()
    daily_dico["longitude"] = response.Longitude()
    daily_dico["elevation"] = response.Elevation()
    return pd.DataFrame(daily_dico)


if __name__ == "__main__":
    # Basic example usage
    os.makedirs("src", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    latitudes = [4.688646]
    longitudes = [-74.212558]
    
    start_date = "2020-01-01"
    end_date = "2024-12-31"
    responses = request_om_data(longitudes, latitudes, start_date, end_date)
    tables = []
    for response in responses:
        df = om_response_to_df(response)
        tables.append(df)
    # Concatenate all the DFs into a single one
    df_responses = pd.concat(tables, ignore_index=True)
    df_responses.to_csv("src/raw_om_data.csv", encoding="UTF-8", index = False)
    
    # The API free limit is 300 000 calls/month and the most expensive plan limit is 5 000 000 calls/month.