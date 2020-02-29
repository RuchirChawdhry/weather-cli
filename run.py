#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# script by Ruchir Chawdhry
# released under MIT License
# github.com/RuchirChawdhry/Python
# ruchirchawdhry.com
# linkedin.com/in/RuchirChawdhry

from weather_terminal_app import view
from weather_terminal_app import controller
from weather_terminal_app.view.view import TodaysWeather

if __name__ == "__main__":
    w = TodaysWeather()
    w.display()
    # table = controller.OpenWeather()
    # print(table)
