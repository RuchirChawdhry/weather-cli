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
    "endpoints": [
        {
            "openweather": "http://api.openweathermap.org/data/2.5/weather/",
            "darksky": None,
        }
    ],
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


def read_config(file_path=DEFAULT_PATH["unix"]):
    if path.exists(file_path):
        with open("config.yml", "r") as f:
            data = load(f, Loader=Loader)
        return data
    else:
        return "Either the file does not exist, is not valid, or is not accessible."


def load_config(file_path):
    error_msg = "Either the file does not exist, is not valid, is not accessible."
    config = file_path if path.exists(file_path) else error_msg
    with open("config.yml", "w") as f:
        data = dump(config, f)
    return data


def read_value(config, value):
    config = read_config(DEFAULT_PATH["unix"])
    return config[value]


def update_value(config, key, value):
    config = load_config(DEFAULT_PATH["unix"])
    updated = config.update({key: value})
    with open("config.yml", "w") as f:
        dump(updated, f)
    return "Updated config!"
