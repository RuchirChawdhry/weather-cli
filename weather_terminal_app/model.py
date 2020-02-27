#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from os import getlogin
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

# //TODO: Changed settings will be in green and unchanged ones in a neutral color.
# //TODO: Make this class based (derived from dict) and more OO.
# //TODO: Make use of magic methods like setitem, delitem.


DEFAULTS = {
    "active_api": "openweather",
    "providers": ["openweather", "darksky", "noaa"],
    "endpoints": {
        "openweather": "http://api.openweathermap.org/data/2.5/weather/",
        "darksky": None,
    },
    "units": "metric",
    "api_keys": ["", ""],  # 1st openweather, 2nd darksky
    "city": "Jaisalmer",
    "state": "Rajasthan",  # equivalent to province
    "country": "India",
    "zipcode": 10017,
    "latitude": "19.0760N",
    "longitude": "72.8777E",
    "first_view": None,  # //TODO: Different views to be implemented
}

DEFAULT_PATH = {"unix": f"~/Users/{getlogin()}/.weather/", "windows": None}


class DefaultConfig:
    def __init__(self):
        self._defaults = DEFAULTS
        self._path = DEFAULT_PATH

    def __str__(self):
        return ", ".join(map(str, self._defaults, self._path))

    def __repr__(self):
        return f"{self.__class__.__name__}(defaults_config={self._defaults!r}, default_path={self._path!r}"

    @staticmethod
    def read_config(file_path=DEFAULT_PATH["unix"]):
        if path.exists(file_path):
            with open("config.yml", "r") as f:
                data = load(f, Loader=Loader)
            return data

    @staticmethod
    def load_config(file_path):
        error_msg = "Either the file does not exist, is not valid, is not accessible."
        config = file_path if path.exists(file_path) else error_msg
        with open("config.yml", "w") as f:
            data = dump(config, f)
        return data


class Config(dict):
    def __init__(self, *args, **kwargs):
        # self.update(*args, **kwargs)
        self._exists = path.exists(DEFAULT_PATH["unix"])
        self._path = DEFAULT_PATH
        self._defaults = DEFAULTS

    def __getitem__(self, key):
        return dict.__getitem__(self._defaults, key)

    def __setitem__(self, key, val):
        return dict.__setitem__(self, key, val)

    def get(self, key, val):
        with open("config.yml", "r") as f:
            data = load(f, Loader=Loader)
        return data[key]

    def update(self, key, val):
        with open("config.yml", "r") as f:
            data = load(f, Loader=Loader)
            data[key] == val
        with open("config.yml", "w") as f:
            dump(data, f)

    def __str__(self):
        return f""

    def __repr__(self):
        pass

    # def __len__(self, **kwargs):
    #     return len(self._keys)

    # def __getitem__(self, key):
    #     return self.__dict__[key]

    def __setitem__(self, key, val):
        return self.__dict__[key] == val
