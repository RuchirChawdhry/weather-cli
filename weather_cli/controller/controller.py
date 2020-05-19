#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import requests as req
from cnamedtuple import namedtuple
from requests_cache import install_cache

from model.model import Config


class API:
    pass


class OpenWeather:
    def __init__(self, city="Mumbai"):
        conf = Config()
        self.endpoint = conf["endpoints"]["openweather"]
        self.units = conf["units"]
        self.session = req.Session()
        self.session.params = {
            "q": city,
            "appid": conf["api_keys"][0],
            "units": conf["units"],
        }

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def _response(self):
        install_cache("cache", backend="sqlite", expire_after=180)
        _json = self.__dict__
        return self.session.get(url=self.endpoint)

    @property
    def wind(self):
        r = self._response().json()
        self.wind_speed, self.wind_deg = r.get("wind").values()
        return namedtuple("wind", ["speed", "deg"])(self.wind_speed, self.wind_deg)

    def coords(self):
        r = self._response().json()
        longitude, latitude = r.get("coord").values()
        return namedtuple("coords", ["latitude", "longitude"])(latitude, longitude)

    @property
    def latitude(self):
        r = self._response().json()
        return r.get("coord").get("latitude")

    @property
    def longitude(self):
        r = self._response().json()
        return r.get("coord").get("longitude")

    @property
    def cloudcover(self):
        r = self._response().json()
        return r.get("clouds").get("all")

    @property
    def weather(self):
        r = self._response().json()
        d = r.pop("main")
        feels_like = d["feels_like"]
        humidity = d["humidity"]
        return namedtuple("weather", ["feels", "min", "max", "humid", "pressure"])(
            feels_like, d["temp_min"], d["temp_max"], humidity, d["pressure"]
        )

    @property
    def sunrise(self):
        r = self._response().json()
        sunrise = datetime.fromtimestamp(r["sys"].get("sunrise")).strftime("%H:%M")
        return sunrise  # UTC

    @property
    def sunset(self):
        r = self._response().json()
        sunset = datetime.fromtimestamp(r["sys"].get("sunset")).strftime("%H:%M")
        return sunset  # UTC

    @property
    def desc(self):
        r = self._response().json()
        w_id, main, desc, icon = r.get("weather")[0].values()
        return namedtuple("weather", ["id", "main", "desc", "icon"])(
            w_id, main, desc, icon
        )

    @property
    def visibility(self):
        r = self._response().json()
        return r.get("visibility")

    def metadata(self):
        r = self._response().json()
        return {
            key: r[key]
            for key in r.keys()
            - {"clouds", "weather", "main", "wind", "coord", "sys", "clouds"}
        }

    @property
    def tzone(self):
        r = self._response().json()
        return timedelta(seconds=r.get("timezone"))
