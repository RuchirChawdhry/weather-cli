#!/usr/bin/env python3

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from weather_terminal_app import controllers
from weather_terminal_app import views

if __name__ == "__main__":
    w = views.TodaysWeather()
    w.display()
    table = controllers.OpenWeather()
    print(table)
