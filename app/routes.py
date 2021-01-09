#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Flask routes"""

#From the app module import the app variable
from app import app

# A line prefixed by "@" is a decorator in python
#We are using the route function to map a view function to 
# a route
@app.route("/")
def index():   # The view function that the route maps to.
    return "Hello, World!"


@app.route("/aboutme")
def about_me():
    my_dictionary = dict()
    my_dictionary["first_name"] = "Joel"
    my_dictionary["last_name"] = "Otero"
    my_dictionary["hobbies"] = "Playing video games"
    return my_dictionary

@app.route("/aboutme2")
def about_me_html():
    first_name = "Joel"
    last_name = "Otero"
    hobbies = "Play video games"
    about_me = """<h1>First name: %s; <br>
                    Last name: %s; <br>
                    Hobbies: %s</h1>""" % (
                        first_name,
                        last_name,
                        hobbies)
    return about_me
                    