#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Find Cost of Tile to Cover W x H Floor -
Calculate the total cost of tile it would take to cover a floor plan
of width and height, using a cost entered by the user."""

width_of_floor = \
    float(raw_input('\nPlease enter the width of your floor in meters. >> '
          ))
length_of_floor = \
    float(raw_input('\nPlease enter the length of your floor in meters. >> '
          ))
cost_of_tile = \
    float(raw_input('\nPlease enter the cost of one tile (assumed in euros, will work for any currency.). >> '
          ))
width_of_tile = \
    float(raw_input('\nPlease enter the width of one tile. >> '))
length_of_tile = \
    float(raw_input('\nPlease enter the length of one tile. >> '))

surface_of_floor = length_of_floor * width_of_floor
surface_of_tile = length_of_tile * width_of_tile
nbr_of_tiles = surface_of_floor / surface_of_tile
total_cost_of_tiles = nbr_of_tiles * cost_of_tile

print '\n-> To cover a floor of ', width_of_floor, '*', \
    length_of_floor, 'm, using tiles of ', width_of_tile, '*', \
    length_of_tile, 'm, that cost ', cost_of_tile, \
    'euros per piece,\n it will cost you ', total_cost_of_tiles, \
    'euros and you will need ', nbr_of_tiles, "tiles. You're welcome."
