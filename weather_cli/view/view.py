#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from click import prompt
from prettytable import PrettyTable

from controller.controller import OpenWeather
from model.model import Config


class TableGen:
    def __init__(self, field_names=[], rows=[], printout=True):
        self.table = PrettyTable()
        self.table.field_names = field_names
        self.table.add_row(rows)

    def generate(self):
        if printout is True:
            print(self.table)
        else:
            return self.table

    def __len__(self):
        return len(self.table.field_names)


class Interactive:
    def __init__(self, city, state, province, country, postal_code, provider):
        self.city = city
        self.state = state
        self.province = province
        self.country = country
        self.postal_code = postal_code
        self.provider = provider

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


class PrettyWeather:
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


class Forecast:
    pass
