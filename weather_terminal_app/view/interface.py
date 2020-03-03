#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plumbum import cli
from plumbum import colors
from weather_terminal_app.controller.controller import OpenWeather
from weather_terminal_app.model.model import Config
from prettytable import PrettyTable
from weather_terminal_app.view.view import TableGen


class WeatherApp(cli.Application):
    PROGNAME = "Clima"
    VERSION = "0.01"
    ALLOW_ABBREV = True

    @cli.switch(["-c", "--city"], str, requires=["--country"])
    def city(self, city):
        w = OpenWeather(city=city)
        print(
            "\n\tCity: " + colors.green[city],
            "Minimum: " + colors.green[str(w.weather.min)] + "°C",
            "Maximum: " + colors.green[str(w.weather.max)] + "°C",
            "Feels Like: " + colors.green[str(w.weather.feels)] + "°C",
            "Wind Speed: " + colors.green[str(w.wind.speed)] + "\n",
            sep="\n\t",
            end="\n",
        )

    @cli.switch(["--country"], str, requires=["--city"])
    def cntry(self, country):
        pass

    @cli.switch(["--zip-code"], int)
    def zip(self, zip_code):
        pass

    @cli.switch(["--lat-lng"])
    def lat_lng(self, lat_lng):
        pass

    @cli.switch("--api-key", int)
    def api(self, api_key):
        pass

    def main(self):
        if self.city or self.cntry:
            print(self.city)
            # rows = [
            #     str(w.weather.min) + "°C",
            #     str(w.weather.max) + "°C",
            #     str(w.weather.feels) + "°C",
            #     w.weather.pressure,
            #     w.wind.speed,
            # ]

            # field_names = ["Feels Like", "Min.", "Max.", "Atm. Pres.", "Wind Speed"]

            # w = OpenWeather(city=city)
            # TableGen(field_names=field_names, rows=rows)
