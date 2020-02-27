#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
from datetime import datetime

from cnamedtuple import namedtuple as cnamedtuple
import requests
from requests_cache import install_cache
from weather_terminal_app.model import Config


class API:
    pass


class OpenWeather:
    def __init__(self, city="Mumbai"):
        conf = Config()
        self.endpoint = conf["endpoints"]["openweather"]
        self.units = conf["units"]
        self.params = {
            "city": city,
            "appid": conf["api_keys"][0],
            "units": conf["units"],
        }

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def _json(self):
        install_cache("cache", backend="sqlite", expire_after=180)
        response = requests.get(url=self.endpoint, params=self.params)
        return response.json()

    @property
    def wind(self):
        r = self._json()
        self.wind_speed, self.wind_deg = r.get("wind").values()
        return cnamedtuple("wind", ["speed", "deg"])(self.wind_speed, self.wind_deg)

    def coords(self):
        r = self._json()
        longitude, latitude = r.get("coord").values()
        return cnamedtuple("coords", ["latitude", "longitude"])(latitude, longitude)

    @property
    def latitude(self):
        r = self._json()
        return r.get("coord").get("latitude")

    @property
    def longitude(self):
        r = self._json()
        return r.get("coord").get("longitude")

    @property
    def cloudcover(self):
        r = self._json()
        return r.get("clouds").get("all")

    @property
    def weather(self):
        r = self._json()
        t_now, pressure, humidity, t_min, t_max = r.get("main").values()
        return cnamedtuple("weather", ["now", "min", "max", "humid", "pressure"])(
            t_now, t_min, t_max, humidity, pressure
        )

    @property
    def sunrise(self):
        r = self._json()
        sunrise = datetime.fromtimestamp(r["sys"].get("sunrise")).strftime("%H:%M")
        return sunrise  # UTC

    @property
    def sunset(self):
        r = self._json()
        sunset = datetime.fromtimestamp(r["sys"].get("sunset")).strftime("%H:%M")
        return sunset  # UTC

    @property
    def desc(self):
        r = self._json()
        w_id, main, desc, icon = r.get("weather")[0].values()
        return cnamedtuple("weather", ["id", "main", "desc", "icon"])(
            w_id, main, desc, icon
        )

    @property
    def visibility(self):
        r = self._json()
        return r.get("visibility")

    def metadata(self):
        r = self._json()
        _r = {
            key: r[key]
            for key in r.keys()
            - {"clouds", "weather", "main", "wind", "coord", "sys", "clouds"}
        }
        visibility, name, base, timezone, id_, cod, dt = _r.values()
        return _r

    @property
    def tzone(self):
        r = self._json()
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
