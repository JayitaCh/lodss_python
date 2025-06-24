#!/bin/python3
from p5 import *
from lodss_python.make_planet import make_planet

def draw_sun():
    fill(255, 255, 0)  # Yellow
    ellipse(width / 2 , height / 2, 100, 100)


# draw_orbits function
def draw_orbits():
    no_fill()
    stroke(255) # Make it white

    for i in range(len(planets)):
        ellipse(width / 2, height / 2, planets[i]['orbit'], planets[i]['orbit'])  

# draw_planets function
def draw_planets():
    for planet in planets:
        colour = planet['colour']
        orbit = planet['orbit']
        size = planet['size']
        speed = planet['speed']
        make_planet(colour, orbit,size,speed)

# load_planets function
planets = []
def load_planets():
    global planets
    with open('planets.csv') as f:
        data = f.read()
        lines = data.splitlines()
    for i in range(1,len(lines)):
        planet_data = lines[i].split(',')
        planet = {
        'name': planet_data[0],
        'colour': Color(int(planet_data[1]), int(planet_data[2]), int(planet_data[3])),  # Make them numbers
        'size': int(planet_data[4]),  # int() for whole numbers
        'orbit': int(planet_data[5]),
        'speed': float(planet_data[6]),  # float() for decimals
        'info': planet_data[7]}
        planets.append(planet) 
  
  
def setup():
    # Put code to run once here
    size(1000, 1000)
  
def draw():
    # Put code to run every frame here
    background(0)
    no_stroke()
    draw_sun()
    load_planets()
    draw_orbits()
    draw_planets()    


def mouse_pressed():
    # Put code to run when the mouse is pressed here
    pixel_colour = Color(get(mouse_x, mouse_y)).hex  # Here the RGB value is converted to Hex so it can be used in a string comparison later
    for planet in planets:
        if pixel_colour == planet['colour'].hex:
            print(planet['name'])
            print(planet['info'])
  
run(frame_rate=20)

