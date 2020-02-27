#!/usr/bin/env python3

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from weather_terminal_app import controller
from weather_terminal_app import view

if __name__ == "__main__":
    w = view.TodaysWeather()
    w.display()
    table = controller.OpenWeather()
    print(table)
