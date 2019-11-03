#!/usr/bin/env python3


from datetime import timedelta

import attr
from cnamedtuple import namedtuple as cnamedtuple
import pendulum
import requests
from requests_cache import install_cache


@attr.s
class API(object):
    city = attr.ib(default=None)
    state = attr.ib(default=None)
    province = attr.ib(default=None)
    country = attr.ib(default=None)
    postal_code = attr.ib(default=None)
    key = attr.ib(default=None)
    provider = attr.ib(default="OpenWeather")


@attr.s(slots=True)
class OpenWeather(API):
    units = attr.ib(default="metric")

    def _json(self):
        install_cache("cache", backend="sqlite", expire_after=180)
        url = "http://api.openweathermap.org/data/2.5/weather/"
        params = {"q": self.city, "appid": self.key, "units": self.units}
        response = requests.get(url, params=params).json()
        return response

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
        sunrise = r.get("sys").get("sunrise")
        sunrise = pendulum.from_timestamp(sunrise).time()
        return sunrise

    @property
    def sunset(self):
        r = self._json()
        sunset = r.get("sys").get("sunset")
        sunset = pendulum.from_timestamp(sunset).time()
        return sunset

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
        return sr.get("visibility")

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


class DarkSkyAPI:
    pass
