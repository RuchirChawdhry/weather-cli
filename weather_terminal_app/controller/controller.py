#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
from datetime import datetime

from cnamedtuple import namedtuple as cnamedtuple
import requests
from requests_cache import install_cache
from weather_terminal_app.model.model import Config


class API:
    pass


class OpenWeather:
    def __init__(self, city="Mumbai"):
        conf = Config()
        self.endpoint = conf["endpoints"]["openweather"]
        self.units = conf["units"]
        self.params = {
            "q": city,
            "appid": conf["api_keys"][0],
            "units": conf["units"],
        }

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def _resp(self):
        install_cache("cache", backend="sqlite", expire_after=180)
        response = requests.get(url=self.endpoint, params=self.params)
        _json = self.__dict__
        return response

    @property
    def wind(self):
        r = self._resp().json()
        self.wind_speed, self.wind_deg = r.get("wind").values()
        return cnamedtuple("wind", ["speed", "deg"])(self.wind_speed, self.wind_deg)

    def coords(self):
        r = self._resp().json()
        longitude, latitude = r.get("coord").values()
        return cnamedtuple("coords", ["latitude", "longitude"])(latitude, longitude)

    @property
    def latitude(self):
        r = self._resp().json()
        return r.get("coord").get("latitude")

    @property
    def longitude(self):
        r = self._resp().json()
        return r.get("coord").get("longitude")

    @property
    def cloudcover(self):
        r = self._resp().json()
        return r.get("clouds").get("all")

    @property
    def weather(self):
        r = self._resp().json()
        d = r.pop("main")
        feels_like = d["feels_like"]
        humidity = d["humidity"]
        return cnamedtuple("weather", ["feels", "min", "max", "humid", "pressure"])(
            d["feels_like"], d["temp_min"], d["temp_max"], d["humidity"], d["pressure"]
        )

    @property
    def sunrise(self):
        r = self._resp().json()
        sunrise = datetime.fromtimestamp(r["sys"].get("sunrise")).strftime("%H:%M")
        return sunrise  # UTC

    @property
    def sunset(self):
        r = self._resp().json()
        sunset = datetime.fromtimestamp(r["sys"].get("sunset")).strftime("%H:%M")
        return sunset  # UTC

    @property
    def desc(self):
        r = self._resp().json()
        w_id, main, desc, icon = r.get("weather")[0].values()
        return cnamedtuple("weather", ["id", "main", "desc", "icon"])(
            w_id, main, desc, icon
        )

    @property
    def visibility(self):
        r = self._resp().json()
        return r.get("visibility")

    def metadata(self):
        r = self._resp().json()
        _r = {
            key: r[key]
            for key in r.keys()
            - {"clouds", "weather", "main", "wind", "coord", "sys", "clouds"}
        }
        visibility, name, base, timezone, id_, cod, dt = _r.values()
        return _r

    @property
    def tzone(self):
        r = self._resp().json()
        return timedelta(seconds=r.get("timezone"))

    def __add__(self, other):
        pass

    def __radd__(self, other):
        return OpenWeather.__add__(self, other)


class DarkSky:
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        return DarkSky.__add__(self, other)
