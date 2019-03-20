#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Some funky colors and sh*t
OKBLUE = '\x1b[1;34;38m'
OKGREEN = '\x1b[1;32;38m'
ALARM = '\x1b[1;33;38m'
FAIL = '\x1b[1;31;38m'
INFO = '\x1b[1;35;38m'
UNDERLINE = "\x1b[4;38;38m"
ENDC = '\x1b[0m'

# Get #portions
def getNPortions():
	in_value = input("Number of portions = ")
	try:
		n_portions = int(in_value)
		
		if n_portions > 0:
			return int(n_portions)
		else:
			print (FAIL+"Give me a frickin\' neat number, mate.."+ENDC)
			return getNPortions()
	except ValueError:
		print (FAIL+"Give me a frickin\' neat number, mate.."+ENDC)
		return getNPortions()


# Basic ingredients
flour = 1500.
water = 1000.
yeast = 5.
honey = 10.
oil   = 50.
salt  = 25.

total = flour + water + yeast + honey + oil + salt

n_portions = -999

print ("\n----------------------------------------")
print ("How many portions of Pizza-dough(à 250g) would you like to have?")

n_portions = getNPortions()

total_input = float(n_portions)*250.
scale = total_input / total

print ("\n#######################")
print ("For "+str(n_portions)+" portions("+str(round(total_input, 0))+"g) of dough use..")
print (" - Flour (Type '00') : "+str(round(flour*scale, 1))+"g --> (batch 1 : "+str(round(flour*scale*2./3., 1))+", batch 2 : "+str(round(flour*scale/3., 1))+")")
print (" - Water :             "+str(round(water*scale, 1))+"g")
print (" - Dry Yeast :         "+str(round(yeast*scale, 1))+"g")
print (" - Honey :             "+str(round(honey*scale, 1))+"g")
print (" - Olive Oil :         "+str(round(oil*scale, 1))+"g")
print (" - Salt :              "+str(round(salt*scale, 1))+"g")
print ("#######################\n")
print (""" --- This is how you do it ---
 """+OKBLUE+"""- Step 1 :"""+ENDC+""" Mix water(room temp.) with honey and dry yeast until the yeast has completely dissolved. Add the first batch of flour and mix till you get a smooth dough.\n
 """+OKBLUE+"""%%%"""+ENDC+""" Cover"""+INFO+"""*"""+ENDC+""" and let rest for ONE hour.\n
 """+OKBLUE+"""- Step 2 :"""+ENDC+""" Add the second batch of flour, as well as the oil and salt to the dough and mix carefully till you get a smooth and flexible dough.\n
 """+OKBLUE+"""%%%"""+ENDC+""" Cover"""+INFO+"""*"""+ENDC+""" and let rest for ONE hour.\n
 """+OKBLUE+"""- Step 3 :"""+ENDC+""" Form """+str(n_portions)+""" dough balls(á 250g) and loosely cover with a bit of extra flour.\n
 """+OKBLUE+"""%%%"""+ENDC+""" Cover"""+INFO+"""*"""+ENDC+""" and let rest for SIX-EIGHT hours"""+INFO+"""**"""+ENDC+""".\n
 - You are good to go now and the remaining dough can live in the fridge until you decide to use it :-)\n\n""")
print (INFO+"*: Mostly airtight to prevent the surface from drying out."+ENDC)
print (INFO+"**: Merely a recommendation of sorts.. actually strongly depends on the amount of yeast you've used.. I mean, don\'t let it rest till it looks like a blobfish, will you!"+ENDC)
print ("----------------------------------------\n")
