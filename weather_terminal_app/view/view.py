#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import attr
from click import prompt
from prettytable import PrettyTable
import questionary

from weather_terminal_app.controller.controller import OpenWeather
from weather_terminal_app.model.model import Config


@attr.s
class Prompts(object):
    city = attr.ib(default=None)
    state = attr.ib(default=None)
    province = attr.ib(default=None)
    country = attr.ib(default=None)
    postal_code = attr.ib(default=None)
    provider = attr.ib(default="OpenWeather")

    def initial_prompt(self):
        self.city = prompt("City? ", default="New Delhi", type=str)
        self.country = prompt("Country? ", default="India", type=str)
        return self.city, self.country

    def choose_provider(self):
        self.provider = questionary.select(
            "Choose a Weather Data Provider: ", choices=["OpenWeatherMap", "DarkSky"]
        ).ask()
        return self.provider

    def openweatherkey(self):
        return questionary.text("Enter your OpenWeatherMap API Key: ")

    def darkskykey(self):
        return questionary.text("Enter your DarkSky API Key: ")


@attr.s
class TodaysWeather:
    def display(self):
        config = Config()

        prompts = Prompts()
        prompts = prompts.initial_prompt()
        city, country = prompts

        w = OpenWeather(city=city)

        table = PrettyTable()
        table.field_names = ["Feels Like", "Min.", "Max.", "Atm. Pres.", "Wind Speed"]
        table.add_row(
            [
                str(w.weather.feels) + "°C",
                str(w.weather.min) + "°C",
                str(w.weather.max) + "°C",
                w.weather.pressure,
                w.wind.speed,
            ]
        )
        print(table)


@attr.s
class HistoricalWeather:
    pass
