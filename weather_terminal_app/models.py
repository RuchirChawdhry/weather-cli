#!/usr/bin/env python3


from vyper import v
from weather_terminal_app import views


class Config(object):
    def default_config(self):
        v.set_config_type("json")
        v.set_config_name("config")
        v.add_config_path(".")
        v.set_default("Active API", "OpenWeatherMap")
        v.set_default("OpenWeatherMap API Key", "")
        v.set_default("DarkSkyWeather API Key", "")
        v.set_default("Key", "")

    def change_config(self):
        answers = views.Prompts()
        v.set("Active API", answers.choose_provider)
        if answers.choose_provider.lower() == "openweathermap":
            v.set("Key", answers.openweatherkey)
        else:
            v.set("key", answers.darkskykey)
        v.set("OpenWeatherMap API Key", answers.openweatherkey)
        v.set("DarkSky API Key", answers.darkskykey)

    def get_config(self):
        v.set_config_name("config")
        v.add_config_path("/usr/local/bin/Weather-Terminal-App")
        v.add_config_path(".")
        v.read_in_config()

    @classmethod
    def key(cls):
        v.add_config_path(".")
        v.set_config_type("json")
        v.read_in_config()
        v.watch_config()
        return v.get("Key")        

