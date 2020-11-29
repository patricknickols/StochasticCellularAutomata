import random
import numpy

states = {"Alabama" : 0.2, "Arizona": -0.4, "Arkansas": 0, "California": -1.1, "Colorado": -4.1, 
"Connecticut": -0.6, "Delaware": 3.4, "Florida": 0.4, "Georgia": -0.9, "Idaho": -1.7, 
"Illinois": 1.1, "Indiana": 2.3, "Iowa": 1.2, "Kansas": 0, "Kentucky": 1.7, "Louisiana": 1.3,
"Maine": -0.1, "Maryland": -0.2, "Massachusetts": -0.9, "Michigan": 2.2, "Minnesota": -0.7, 
"Mississippi": 3, "Missouri": 0.3, "Montana": -2.6, "Nebraska": 0.3, "Nevada": 0, 
"New Hampshire": -1.1, "New Jersey": 0, "New Mexico": -2.9, "New York": -1.7, "North Carolina": 1.3,
"North Dakota": 0.6, "Ohio": 0.3, "Oklahoma": -0.7, "Oregon": 0.2, "Pennsylvania": 2.7,
"Rhode Island": -0.9, "South Carolina": 1, "South Dakota": -0.3, "Tennessee": 0.1,
"Texas": -0.3, "Utah": -2, "Vermont": -0.3, "Virginia": 0.3, "Washington": -0.9,
"West Virginia": 2.7, "Wisconsin": 0.8, "Wyoming": 0}

states_1990 = {"Alabama" : 0.2, "Arizona": -0.4, "Arkansas": 0, "California": -1.1, "Colorado": -4.1,
"Connecticut": -0.6, "Delaware": 3.4, "Florida": 0.4, "Georgia": -0.9, "Idaho": -1.7, "Illinois": 1.1,
"Indiana": 2.3, "Iowa": 1.2, "Kansas": 0, "Kentucky": 1.7, "Louisiana": 1.3, "Maine": -0.1,
"Maryland": -0.2, "Massachusetts": -0.9, "Michigan": 2.2, "Minnesota": -0.7, "Mississippi": 3,
"Missouri": 0.3, "Montana": -2.6, "Nebraska": 0.3, "Nevada": 0, "New Hampshire": -1.1, "New Jersey": 0,
"New Mexico": -2.9, "New York": -1.7, "North Carolina": 1.3, "North Dakota": 0.6, "Ohio": 0.3,
"Oklahoma": -0.7, "Oregon": 0.2, "Pennsylvania": 2.7, "Rhode Island": -0.9, "South Carolina": 1,
"South Dakota": -0.3, "Tennessee": 0.1, "Texas": -0.3, "Utah": -2, "Vermont": -0.3, "Virginia": 0.3,
"Washington": -0.9, "West Virginia": 2.7, "Wisconsin": 0.8, "Wyoming": 0}


bordering_states = {"Alabama": ["Florida", "Mississippi", "Georgia", "Tennessee"],\
"Arizona": ["California", "Utah", "New Mexico", "Colorado", "Nevada"],\
"Arkansas": ["Mississippi", "Louisiana", "Texas", "Missouri", "Tennessee", "Oklahoma"],\
"California": ["Arizona", "Nevada", "Oregon"],\
"Colorado": ["Arizona", "New Mexico", "Oklahoma", "Kansas", "Nebraska", "Wyoming", "Utah"],\
"Connecticut" : ["Massachusetts", "Rhode Island", "New York"],\
"Delaware" : ["New Jersey", "Pennsylvania", "Maryland"],\
"Florida" : ["Alabama", "Georgia"],\
"Georgia" : ["Florida", "Alabama", "South Carolina", "Tennessee", "North Carolina"],\
"Idaho" : ["Montana", "Washington", "Oregon", "Nevada", "Utah", "Wyoming"],\
"Illinois" : ["Indiana", "Kentucky", "Missouri", "Iowa", "Wisconsin"],\
"Indiana" : ["Michigan", "Illinois", "Kentucky", "Ohio"],\
"Iowa" : ["Minnesota", "Wisconsin", "Illinois", "Missouri", "Nebraska", "South Dakota"],\
"Kansas" : ["Nebraska", "Missouri", "Oklahoma", "Colorado"],\
"Kentucky" : ["West Virginia", "Virginia", "Tennessee", "Missouri", "Illinois", "Indiana", "Ohio"],\
"Louisiana" : ["Mississippi", "Arkansas", "Texas"],\
"Maine" : ["New Hampshire"],\
"Maryland" : ["Delaware", "Virginia", "West Virginia", "Pennsylvania"],\
"Massachusetts" : ["Rhode Island", "New Hampshire", "Vermont", "Connecticut", "New York"],\
"Michigan" : ["Indiana", "Ohio", "Wisconsin"],\
"Minnesota" : ["Wisconsin", "Iowa", "South Dakota", "North Dakota"],\
"Mississippi" : ["Louisiana", "Arkansas", "Alabama", "Tennessee"],\
"Missouri" : ["Arkansas", "Kentucky", "Kansas", "Iowa", "Illinois", "Nebraska", "Tennessee", "Oklahoma"],\
"Montana" : ["Idaho", "Wyoming", "North Dakota", "South Dakota"],\
"Nebraska" : ["Missouri", "Kansas", "Iowa", "Colorado", "Wyoming", "South Dakota"],\
"Nevada" : ["Idaho", "California", "Arizona", "Utah", "Oregon"],\
"New Hampshire" : ["Maine", "Massachusetts", "Vermont"],\
"New Jersey" : ["Delaware", "New York", "Pennsylvania"],\
"New Mexico" : ["Arizona", "Utah", "Colorado", "Texas", "Oklahoma"],\
"New York" : ["New Jersey", "Connecticut", "Massachusetts", "Pennsylvania", "Vermont"],\
"North Carolina" : ["Georgia", "Tennessee", "Virginia", "South Carolina"],\
"North Dakota" : ["Minnesota", "South Dakota", "Montana"],\
"Ohio" : ["Indiana", "Kentucky", "Michigan", "Pennsylvania", "West Virginia",],\
"Oklahoma" : ["Kansas", "Colorado", "New Mexico", "Texas", "Missouri", "Arkansas"],\
"Oregon" : ["Washington", "Idaho", "Nevada", "California"],\
"Pennsylvania" : ["Delaware", "Maryland", "New Jersey", "New York", "Ohio", "West Virginia"],\
"Rhode Island" : ["Massachusetts", "Connecticut"],\
"South Carolina" : ["North Carolina", "Georgia",],\
"South Dakota" : ["North Dakota", "Minnesota", "Iowa", "Nebraska", "Wyoming", "Montana"],\
"Tennessee" : ["Alabama", "Arkansas", "Georgia", "Kentucky", "Mississippi", "Missouri", 
"North Carolina", "Virginia"],\
"Texas" : ["Arkansas", "Louisiana", "New Mexico", "Oklahoma"],\
"Utah" : ["Arizona", "Colorado", "Idaho", "Nevada", "New Mexico", "Wyoming"],\
"Vermont" : ["Massachusetts", "New Hampshire", "New York"],\
"Virginia" : ["Kentucky", "Maryland", "North Carolina", "Tennessee", "West Virginia"],\
"Washington" : ["Idaho", "Oregon"],\
"West Virginia" : ["Kentucky", "Maryland", "Ohio", "Pennsylvania", "Virginia"],\
"Wisconsin" : ["Illinois", "Iowa", "Michigan", "Minnesota"],\
"Wyoming" : ["Colorado", "Idaho", "Montana", "Nebraska", "South Dakota", "Utah"]}


very_fat_states = []
quite_fat_states = []
medium_fat_states = []
little_fat_states = []
just_fat_states = []
neutral_states = []
just_thin_states = []
little_thin_states = []
medium_thin_states = []
quite_thin_states = []
very_thin_states =[]
types_of_places = [very_fat_states, quite_fat_states, medium_fat_states, little_fat_states, 
just_fat_states, neutral_states, just_thin_states, little_thin_states, medium_thin_states,
quite_thin_states, very_thin_states]
def categorise_places(places):                                      #This function sorts states into "levels of obesity" based on their value.
	for place in places:											#in addition it removes the differences between two "very fat states" by setting their values to a common number.
		if places[place] >= 4:
			very_fat_states.append(place)
			places[place] = 4.1
		elif places[place] >= 3 and places[place] < 4:
			quite_fat_states.append(place)
			places[place] = 3.1
		elif places[place] >= 2 and places[place] < 3:
			medium_fat_states.append(place)
			places[place] = 2.1
		elif places[place] >= 1 and places[place] < 2:
			little_fat_states.append(place)
			places[place] = 1.1
		elif places[place] > 0 and places[place] < 1:
			just_fat_states.append(place)
			places[place] =  0.1
		elif places[place] == 0:
			neutral_states.append(place)
		elif places[place] < 0 and places[place] > -1:
			just_thin_states.append(place)
			places[place] = -0.1
		elif places[place] <= -1 and places[place] > -2:
			little_thin_states.append(place)
			places[place] = -1.1
		elif places[place] <= -2 and places[place] > -3:
			medium_thin_states.append(place)
			places[place] = -2.1
		elif places[place] <= -3 and places[place] > -4:
			quite_thin_states.append(place)
			places[place] = -3.1
		elif places[place] <= -4:
			very_thin_states.append(place)
			places[place] =-4.1
		else:
			print "Error! Some state has an invalid value."




Chance_of_increasing_by_1 = {}
Chance_of_increasing_by_2 = {}
Chance_of_increasing_by_3 = {}
Chance_of_increasing_by_4 = {}
Chance_of_increasing_by_5 = {}
Chance_of_increasing_by_6 = {}
Chance_of_increasing_by_7 = {}
Chance_of_increasing_by_8 = {}
Chance_of_increasing_by_9 = {}
Chance_of_increasing_by_10 = {}
Chance_of_decreasing_by_1 = {}
Chance_of_decreasing_by_2 = {}
Chance_of_decreasing_by_3 = {}
Chance_of_decreasing_by_4 = {}
Chance_of_decreasing_by_5 = {}
Chance_of_decreasing_by_6 = {}
Chance_of_decreasing_by_7 = {}
Chance_of_decreasing_by_8 = {}
Chance_of_decreasing_by_9 = {}
Chance_of_decreasing_by_10 = {}
Chance_of_remaining = {}

categorise_places(states)
                                         #This sorts them initially into their groups based on their obesities in the year 1990.

def base_transition_matrix():
	for location in states:                                                       #Populates each dictionary of relevant chances according to the transition matrix initially per state like so: {"Alabama": 1/2}
		if location in very_fat_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 0
			Chance_of_increasing_by_4[location] = 0
			Chance_of_increasing_by_3[location] = 0
			Chance_of_increasing_by_2[location] = 0
			Chance_of_increasing_by_1[location] = 0
			Chance_of_decreasing_by_10[location] = 1.0/2046
			Chance_of_decreasing_by_9[location] = 1.0/1023
			Chance_of_decreasing_by_8[location] = 2.0/1023
			Chance_of_decreasing_by_7[location] = 4.0/1023
			Chance_of_decreasing_by_6[location] = 8.0/1023
			Chance_of_decreasing_by_5[location] = 16.0/1023
			Chance_of_decreasing_by_4[location] = 32.0/1023
			Chance_of_decreasing_by_3[location] = 64.0/1023
			Chance_of_decreasing_by_2[location] = 128.0/1023
			Chance_of_decreasing_by_1[location] = 256.0/1023
			Chance_of_remaining[location] = 0.5
		elif location in quite_fat_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 0
			Chance_of_increasing_by_4[location] = 0
			Chance_of_increasing_by_3[location] = 0
			Chance_of_increasing_by_2[location] = 0
			Chance_of_increasing_by_1[location] = 128.0/767
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 1.0/1534
			Chance_of_decreasing_by_8[location] = 1.0/767
			Chance_of_decreasing_by_7[location] = 2.0/767
			Chance_of_decreasing_by_6[location] = 4.0/767
			Chance_of_decreasing_by_5[location] = 8.0/767
			Chance_of_decreasing_by_4[location] = 16.0/767
			Chance_of_decreasing_by_3[location] = 32.0/767
			Chance_of_decreasing_by_2[location] = 64.0/767
			Chance_of_decreasing_by_1[location] = 128.0/767
			Chance_of_remaining[location] = 0.5
		elif location in medium_fat_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 0
			Chance_of_increasing_by_4[location] = 0
			Chance_of_increasing_by_3[location] = 0
			Chance_of_increasing_by_2[location] = 32.0/447
			Chance_of_increasing_by_1[location] = 64.0/447
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 1.0/894
			Chance_of_decreasing_by_7[location] = 1.0/447
			Chance_of_decreasing_by_6[location] = 2.0/447
			Chance_of_decreasing_by_5[location] = 4.0/447
			Chance_of_decreasing_by_4[location] = 8.0/447
			Chance_of_decreasing_by_3[location] = 16.0/447
			Chance_of_decreasing_by_2[location] = 32.0/447
			Chance_of_decreasing_by_1[location] = 64.0/447
			Chance_of_remaining[location] = 0.5
		elif location in little_fat_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 0
			Chance_of_increasing_by_4[location] = 0
			Chance_of_increasing_by_3[location] = 8.0/239
			Chance_of_increasing_by_2[location] = 16.0/239
			Chance_of_increasing_by_1[location] = 32.0/239
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 1.0/478
			Chance_of_decreasing_by_6[location] = 1.0/239
			Chance_of_decreasing_by_5[location] = 2.0/239
			Chance_of_decreasing_by_4[location] = 4.0/239
			Chance_of_decreasing_by_3[location] = 8.0/239
			Chance_of_decreasing_by_2[location] = 16.0/239
			Chance_of_decreasing_by_1[location] = 32.0/239
			Chance_of_remaining[location] = 0.5
		elif location in just_fat_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 0
			Chance_of_increasing_by_4[location] = 2.0/123
			Chance_of_increasing_by_3[location] = 4.0/123
			Chance_of_increasing_by_2[location] = 8.0/123
			Chance_of_increasing_by_1[location] = 16.0/123
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 1.0/246
			Chance_of_decreasing_by_5[location] = 1.0/123
			Chance_of_decreasing_by_4[location] = 2.0/123
			Chance_of_decreasing_by_3[location] = 4.0/123
			Chance_of_decreasing_by_2[location] = 8.0/123
			Chance_of_decreasing_by_1[location] = 16.0/123
			Chance_of_remaining[location] = 0.5
		elif location in neutral_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 0
			Chance_of_increasing_by_5[location] = 1.0/124
			Chance_of_increasing_by_4[location] = 1.0/62
			Chance_of_increasing_by_3[location] = 1.0/31
			Chance_of_increasing_by_2[location] = 2.0/31
			Chance_of_increasing_by_1[location] = 4.0/31
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 1.0/124
			Chance_of_decreasing_by_4[location] = 1.0/62
			Chance_of_decreasing_by_3[location] = 1.0/31
			Chance_of_decreasing_by_2[location] = 2.0/31
			Chance_of_decreasing_by_1[location] = 4.0/31
			Chance_of_remaining[location] = 0.5
		elif location in just_thin_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 0
			Chance_of_increasing_by_6[location] = 1.0/246
			Chance_of_increasing_by_5[location] = 1.0/123
			Chance_of_increasing_by_4[location] = 2.0/123
			Chance_of_increasing_by_3[location] = 4.0/123
			Chance_of_increasing_by_2[location] = 8.0/123
			Chance_of_increasing_by_1[location] = 16.0/123
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 0
			Chance_of_decreasing_by_4[location] = 2.0/123
			Chance_of_decreasing_by_3[location] = 4.0/123
			Chance_of_decreasing_by_2[location] = 8.0/123
			Chance_of_decreasing_by_1[location] = 16.0/123
			Chance_of_remaining[location] = 0.5
		elif location in little_thin_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 0
			Chance_of_increasing_by_7[location] = 1.0/478
			Chance_of_increasing_by_6[location] = 1.0/239
			Chance_of_increasing_by_5[location] = 2.0/239
			Chance_of_increasing_by_4[location] = 4.0/239
			Chance_of_increasing_by_3[location] = 8.0/239
			Chance_of_increasing_by_2[location] = 16.0/239
			Chance_of_increasing_by_1[location] = 32.0/239
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 0
			Chance_of_decreasing_by_4[location] = 0
			Chance_of_decreasing_by_3[location] = 8.0/239
			Chance_of_decreasing_by_2[location] = 16.0/239
			Chance_of_decreasing_by_1[location] = 32.0/239
			Chance_of_remaining[location] = 0.5
		elif location in medium_thin_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 0
			Chance_of_increasing_by_8[location] = 1.0/894
			Chance_of_increasing_by_7[location] = 1.0/447
			Chance_of_increasing_by_6[location] = 2.0/447
			Chance_of_increasing_by_5[location] = 4.0/447
			Chance_of_increasing_by_4[location] = 8.0/447
			Chance_of_increasing_by_3[location] = 16.0/447
			Chance_of_increasing_by_2[location] = 32.0/447
			Chance_of_increasing_by_1[location] = 64.0/447
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 0
			Chance_of_decreasing_by_4[location] = 0
			Chance_of_decreasing_by_3[location] = 0
			Chance_of_decreasing_by_2[location] = 32.0/447
			Chance_of_decreasing_by_1[location] = 64.0/447
			Chance_of_remaining[location] = 0.5
		elif location in quite_thin_states:
			Chance_of_increasing_by_10[location] = 0
			Chance_of_increasing_by_9[location] = 1.0/1534
			Chance_of_increasing_by_8[location] = 1.0/767
			Chance_of_increasing_by_7[location] = 2.0/767
			Chance_of_increasing_by_6[location] = 4.0/767
			Chance_of_increasing_by_5[location] = 8.0/767
			Chance_of_increasing_by_4[location] = 16.0/767
			Chance_of_increasing_by_3[location] = 32.0/767
			Chance_of_increasing_by_2[location] = 64.0/767
			Chance_of_increasing_by_1[location] = 128.0/767
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 0
			Chance_of_decreasing_by_4[location] = 0
			Chance_of_decreasing_by_3[location] = 0
			Chance_of_decreasing_by_2[location] = 0
			Chance_of_decreasing_by_1[location] = 128.0/767
			Chance_of_remaining[location] = 0.5
		elif location in very_thin_states:
			Chance_of_increasing_by_10[location] = 1.0/2046
			Chance_of_increasing_by_9[location] = 1.0/1023
			Chance_of_increasing_by_8[location] = 2.0/1023
			Chance_of_increasing_by_7[location] = 4.0/1023
			Chance_of_increasing_by_6[location] = 8.0/1023
			Chance_of_increasing_by_5[location] = 16.0/1023
			Chance_of_increasing_by_4[location] = 32.0/1023
			Chance_of_increasing_by_3[location] = 64.0/1023
			Chance_of_increasing_by_2[location] = 128.0/1023
			Chance_of_increasing_by_1[location] = 256.0/1023
			Chance_of_decreasing_by_10[location] = 0
			Chance_of_decreasing_by_9[location] = 0
			Chance_of_decreasing_by_8[location] = 0
			Chance_of_decreasing_by_7[location] = 0
			Chance_of_decreasing_by_6[location] = 0
			Chance_of_decreasing_by_5[location] = 0
			Chance_of_decreasing_by_4[location] = 0
			Chance_of_decreasing_by_3[location] = 0
			Chance_of_decreasing_by_2[location] = 0
			Chance_of_decreasing_by_1[location] = 0
			Chance_of_remaining[location] = 0.5

base_transition_matrix()
"""
print "Chance of decreasing by 1" + str(Chance_of_decreasing_by_1)
print "Very fat:" + str(very_fat_states)
print "Quite fat:" + str(quite_fat_states)
print "Medium fat:" + str(medium_fat_states)
print "Little fat:" + str(little_fat_states)
print "Just fat:" + str(just_fat_states)                        #Commented out test to see if categorise_places and base_transition_matrix are fully functional.
print "Netural:" + str(neutral_states)
print "Just thin:" + str(just_thin_states)
print "Little thin:" + str(little_thin_states)
print "Medium thin:" + str(medium_thin_states)
print "Quite thin:" + str(quite_thin_states)
print "Very thin:" + str(very_thin_states)
print "Chance of increasing by 1" + str(Chance_of_increasing_by_1)
"""


def probability_change_very_fat(location):                                       #Updates the dictionary with new probabilities
	d = 0.2
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] += d
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] += (d/2)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_2[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] += (d/4)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_3[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] += (d/8)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_4[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] += (d/16)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_5[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] += (d/32)
	elif Chance_of_increasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_6[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] += (d/64)
	elif Chance_of_increasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_7[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] += (d/128)
	elif Chance_of_increasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_8[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] += (d/256)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_9[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] += (d/512)
	elif Chance_of_increasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_10[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_2[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_3[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_4[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_5[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_6[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_7[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_8[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_9[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_10[location])

	Chance_of_remaining[location] -= d * (1023/1024)

def probability_change_quite_fat(location):
	d = 0.15
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] += d
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] += (d/2)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_2[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] += (d/4)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_3[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] += (d/8)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_4[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] += (d/16)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_5[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] += (d/32)
	elif Chance_of_increasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_6[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] += (d/64)
	elif Chance_of_increasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_7[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] += (d/128)
	elif Chance_of_increasing_by_8[location] == 0:
			Chance_of_remaining[location] += (d/128)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_8[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] += (d/256)
	elif Chance_of_increasing_by_9[location] == 0:
			Chance_of_remaining[location] += (d/256)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_9[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] += (d/512)
	elif Chance_of_increasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_10[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_2[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_3[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_4[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_5[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_6[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_7[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_8[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_9[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_10[location])

	Chance_of_remaining[location] -= d * (1023/1024)

def probability_change_medium_fat(location):
	d = 0.1
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] += d
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] += (d/2)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_2[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] += (d/4)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_3[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] += (d/8)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_4[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] += (d/16)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_5[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] += (d/32)
	elif Chance_of_increasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_6[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] += (d/64)
	elif Chance_of_increasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_7[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] += (d/128)
	elif Chance_of_increasing_by_8[location] == 0:
			Chance_of_remaining[location] += (d/128)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_8[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] += (d/256)
	elif Chance_of_increasing_by_9[location] == 0:
			Chance_of_remaining[location] += (d/256)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_9[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] += (d/512)
	elif Chance_of_increasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_10[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_2[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_3[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_4[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_5[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_6[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_7[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_8[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_9[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_10[location])

	Chance_of_remaining[location] -= d * (1023/1024)

def probability_change_little_fat(location):
	d = 0.075
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] += d
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] += (d/2)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_2[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] += (d/4)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_3[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] += (d/8)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_4[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] += (d/16)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_5[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] += (d/32)
	elif Chance_of_increasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_6[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] += (d/64)
	elif Chance_of_increasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_7[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] += (d/128)
	elif Chance_of_increasing_by_8[location] == 0:
			Chance_of_remaining[location] += (d/128)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_8[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] += (d/256)
	elif Chance_of_increasing_by_9[location] == 0:
			Chance_of_remaining[location] += (d/256)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_9[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] += (d/512)
	elif Chance_of_increasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_10[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_2[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_3[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_4[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_5[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_6[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_7[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_8[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_9[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_10[location])

	Chance_of_remaining[location] -= d * (1023/1024)

def probability_change_just_fat(location):
	d = 0.05
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] += d
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] += (d/2)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_2[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] += (d/4)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_3[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] += (d/8)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_4[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] += (d/16)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_5[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] += (d/32)
	elif Chance_of_increasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_6[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] += (d/64)
	elif Chance_of_increasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_7[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] += (d/128)
	elif Chance_of_increasing_by_8[location] == 0:
			Chance_of_remaining[location] += (d/128)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_8[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] += (d/256)
	elif Chance_of_increasing_by_9[location] == 0:
			Chance_of_remaining[location] += (d/256)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_9[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] += (d/512)
	elif Chance_of_increasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_increasing_by_10[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_2[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_3[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_4[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_5[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_6[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_7[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_8[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_9[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_10[location])

	Chance_of_remaining[location] -= d * (1023/1024)

def probability_change_neutral(location):
	return

def probability_change_very_thin(location):
	d = 0.2
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] -= (d/64)
	elif Chance_of_increasing_by_6[location]== 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] -= (d/128)
	elif Chance_of_increasing_by_7[location]== 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] -= (d/256)
	elif Chance_of_increasing_by_8[location]== 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location]== 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] += d
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])


	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	Chance_of_remaining[location] -= Chance_of_increasing_by_1[location] * (1023/1024)

def probability_change_quite_thin(location):
	d  = 0.15
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] -= (d/64)
	elif Chance_of_increasing_by_6[location]== 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] -= (d/128)
	elif Chance_of_increasing_by_7[location]== 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] -= (d/256)
	elif Chance_of_increasing_by_8[location]== 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location]== 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] += d
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])


	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	Chance_of_remaining[location] -= Chance_of_increasing_by_1[location] * (1023/1024)

def probability_change_medium_thin(location):
	d = 0.1
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] -= (d/64)
	elif Chance_of_increasing_by_6[location]== 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] -= (d/128)
	elif Chance_of_increasing_by_7[location]== 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] -= (d/256)
	elif Chance_of_increasing_by_8[location]== 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location]== 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] += d
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])


	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	Chance_of_remaining[location] -= Chance_of_increasing_by_1[location] * (1023/1024)

def probability_change_little_thin(location):
	d = 0.075
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] -= (d/64)
	elif Chance_of_increasing_by_6[location]== 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] -= (d/128)
	elif Chance_of_increasing_by_7[location]== 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] -= (d/256)
	elif Chance_of_increasing_by_8[location]== 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location]== 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] += d
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])


	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	Chance_of_remaining[location] -= Chance_of_increasing_by_1[location] * (1023/1024)

def probability_change_just_thin(location):
	d = 0.05
	if Chance_of_increasing_by_1[location] > 0:
		Chance_of_increasing_by_1[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] == 0:
		Chance_of_remaining[location] -= (d/2)
	elif Chance_of_increasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_2[location] > 0:
		Chance_of_increasing_by_2[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] == 0:
		Chance_of_remaining[location] -= (d/4)
	elif Chance_of_increasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_3[location] > 0:
		Chance_of_increasing_by_3[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] == 0:
		Chance_of_remaining[location] -= (d/8)
	elif Chance_of_increasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_4[location] > 0:
		Chance_of_increasing_by_4[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] == 0:
		Chance_of_remaining[location] -= (d/16)
	elif Chance_of_increasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_5[location] > 0:
		Chance_of_increasing_by_5[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] == 0:
		Chance_of_remaining[location] -= (d/32)
	elif Chance_of_increasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_6[location] > 0:
		Chance_of_increasing_by_6[location] -= (d/64)
	elif Chance_of_increasing_by_6[location]== 0:
		Chance_of_remaining[location] -= (d/64)
	elif Chance_of_increasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_7[location] > 0:
		Chance_of_increasing_by_7[location] -= (d/128)
	elif Chance_of_increasing_by_7[location]== 0:
		Chance_of_remaining[location] -= (d/128)
	elif Chance_of_increasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_8[location] > 0:
		Chance_of_increasing_by_8[location] -= (d/256)
	elif Chance_of_increasing_by_8[location]== 0:
		Chance_of_remaining[location] -= (d/256)
	elif Chance_of_increasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_9[location] > 0:
		Chance_of_increasing_by_9[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] == 0:
		Chance_of_remaining[location] -= (d/512)
	elif Chance_of_increasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_increasing_by_10[location] > 0:
		Chance_of_increasing_by_10[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location]== 0:
		Chance_of_remaining[location] -= (d/1024)
	elif Chance_of_increasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_1[location] > 0:
		Chance_of_decreasing_by_1[location] += d
	elif Chance_of_decreasing_by_1[location] == 0:
		Chance_of_remaining[location] += d
	elif Chance_of_decreasing_by_1[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])


	elif Chance_of_decreasing_by_2[location] > 0:
		Chance_of_decreasing_by_2[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] == 0:
		Chance_of_remaining[location] += (d/2)
	elif Chance_of_decreasing_by_2[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_3[location] > 0:
		Chance_of_decreasing_by_3[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] == 0:
		Chance_of_remaining[location] += (d/4)
	elif Chance_of_decreasing_by_3[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_4[location] > 0:
		Chance_of_decreasing_by_4[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] == 0:
		Chance_of_remaining[location] += (d/8)
	elif Chance_of_decreasing_by_4[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_5[location] > 0:
		Chance_of_decreasing_by_5[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] == 0:
		Chance_of_remaining[location] += (d/16)
	elif Chance_of_decreasing_by_5[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_6[location] > 0:
		Chance_of_decreasing_by_6[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] == 0:
		Chance_of_remaining[location] += (d/32)
	elif Chance_of_decreasing_by_6[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_7[location] > 0:
		Chance_of_decreasing_by_7[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] == 0:
		Chance_of_remaining[location] += (d/64)
	elif Chance_of_decreasing_by_7[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_8[location] > 0:
		Chance_of_decreasing_by_8[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] == 0:
		Chance_of_remaining[location] += (d/128)
	elif Chance_of_decreasing_by_8[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_9[location] > 0:
		Chance_of_decreasing_by_9[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] == 0:
		Chance_of_remaining[location] += (d/256)
	elif Chance_of_decreasing_by_9[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	elif Chance_of_decreasing_by_10[location] > 0:
		Chance_of_decreasing_by_10[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] == 0:
		Chance_of_remaining[location] += (d/512)
	elif Chance_of_decreasing_by_10[location] < 0:
		print "Error. Probability less than 0" + str(location) + ": " + 
		str(Chance_of_decreasing_by_1[location])

	Chance_of_remaining[location] -= Chance_of_increasing_by_1[location] * (1023/1024)

def forward_year_probabilities():
	for state in bordering_states:                                #For each state
			for border_state in bordering_states[state]:		  #For each state that borders those states
				if border_state in very_fat_states:               #if that bordering state is very fat
					probability_change_very_fat(state)	          #Update the original state's probability accordingly
				elif border_state in quite_fat_states:
					probability_change_quite_fat(state)
				elif border_state in medium_fat_states:
					probability_change_medium_fat(state)
				elif border_state in little_fat_states:
					probability_change_little_fat(state)
				elif border_state in just_fat_states:
					probability_change_just_fat(state)
				elif border_state in neutral_states:
					probability_change_neutral(state)
				elif border_state in just_thin_states:
					probability_change_just_thin(state)
				elif border_state in little_thin_states:
					probability_change_little_thin(state)
				elif border_state in medium_thin_states:
					probability_change_medium_thin(state)
				elif border_state in quite_thin_states:
					probability_change_quite_thin(state)
				elif border_state in very_thin_states:
					probability_change_very_thin(state)

Change_of_states = {}

for state in states:
	Change_of_states[state] = []

def forward_year_values():
	simulate_count = 0
	total_simulations = int(raw_input("How many simulations?"))
	while simulate_count < total_simulations:
		x = random.randint(1,1000000)                                                                  #Picks a random integer between 1 and a million
		for state in states:
			a = 1000000 * Chance_of_increasing_by_1[state]	                                                      #Partitions numbers between 1 and a million into sections E.g. Numbers less than 10000 are +1, numbers between 10000 and 20000
			#print "a =" + str(a)
			aa = a + (1000000 * Chance_of_increasing_by_2[state])
			aaa = aa + (1000000 * Chance_of_increasing_by_3[state])
			aaaa = aaa + (1000000 * Chance_of_increasing_by_4[state])
			aaaaa = aaaa + (1000000 * Chance_of_increasing_by_5[state])
			aaaaaa = aaaaa + (1000000 * Chance_of_increasing_by_6[state])
			aaaaaaa = aaaaaa + (1000000 * Chance_of_increasing_by_7[state])
			aaaaaaaa = aaaaaaa + (1000000 * Chance_of_increasing_by_8[state])
			aaaaaaaaa = aaaaaaaa + (1000000 * Chance_of_increasing_by_9[state])
			aaaaaaaaaa = aaaaaaaaa + (10000000 * Chance_of_increasing_by_10[state])
			b = aaaaaaaaaa + (1000000 * Chance_of_decreasing_by_1[state])
			bb = b + (1000000 * Chance_of_decreasing_by_2[state])
			bbb = bb + (1000000 * Chance_of_decreasing_by_3[state])
			bbbb = bbb + (1000000 * Chance_of_decreasing_by_4[state])
			bbbbb = bbbb + (1000000 * Chance_of_decreasing_by_5[state])
			bbbbbb = bbbbb + (1000000 * Chance_of_decreasing_by_6[state])
			bbbbbbb = bbbbbb + (1000000 * Chance_of_decreasing_by_7[state])
			bbbbbbbb = bbbbbbb + (1000000 * Chance_of_decreasing_by_8[state])
			bbbbbbbbb = bbbbbbbb + (1000000 * Chance_of_decreasing_by_9[state])
			bbbbbbbbbb = bbbbbbbbb + (1000000 * Chance_of_decreasing_by_10[state])
			c = 1000000
					#f.write(str(state) + ": \n")
					#f.write("x = " + str(x) +"\n")
					#f.write("a = " + str(a) +"\n")
					#f.write("aa = " + str(aa) +"\n")
					#f.write("aaa = " + str(aaa) +"\n")
					#f.write("aaaa = " + str(aaaa) +"\n")
					#f.write("aaaaa = " + str(aaaaa) +"\n")
					#f.write("aaaaaa = " + str(aaaaaa) +"\n")
					#f.write("aaaaaaa = " + str(aaaaaaa) +"\n")
					#f.write("aaaaaaaa = " + str(aaaaaaaa) +"\n")
					#f.write("aaaaaaaaa = " + str(aaaaaaaa) +"\n")
					#f.write("aaaaaaaaaa = " + str(aaaaaaaaa) +"\n")                           #Commented out test that gaining or losing was appropriately handled
					#f.write("b = " + str(b) +"\n")
					#f.write("bb = " + str(bb) +"\n")
					#f.write("bbb = " + str(bbb) +"\n")
					#f.write("bbbb = " + str(bbbb) +"\n")
					#f.write("bbbbb = " + str(bbbbb) +"\n")
					#f.write("bbbbbb = " + str(bbbbbb) +"\n")
					#f.write("bbbbbbb = " + str(bbbbbbb) +"\n")
					#f.write("bbbbbbbb = " + str(bbbbbbbb) +"\n")
					#f.write("bbbbbbbbb = " + str(bbbbbbbbb) +"\n")
					#f.write("bbbbbbbbbb = " + str(bbbbbbbbbb) +"\n")
					#f.write("c = " + str(c) +"\n")
			if x <= a:
				#states[state] += 1
				Change_of_states[state].append(1)
			elif x > a and x <= aa:
				#states[state] += 2
				Change_of_states[state].append(2)
			elif x > aa and x <= aaa:
				#states[state] += 3
				Change_of_states[state].append(3)
			elif x > aaa and x <= aaaa:
				#states[state] += 4
				Change_of_states[state].append(4)
			elif x > aaaa and x <= aaaaa:
				#states[state] += 5
				Change_of_states[state].append(5)
			elif x > aaaaa and x <= aaaaaa:
				#states[state] += 6
				Change_of_states[state].append(6)
			elif x > aaaaaa and x <= aaaaaaa:
				#states[state] += 7
				Change_of_states[state].append(7)
			elif x > aaaaaaa and x <= aaaaaaaa:
				#states[state] += 8
				Change_of_states[state].append(8)
			elif x > aaaaaaaa and x <= aaaaaaaaa:
				#states[state] += 9
				Change_of_states[state].append(9)
			elif x > aaaaaaaaa and x <= aaaaaaaaaa:
				#states[state] += 10
				Change_of_states[state].append(10)
			elif aaaaaaaaaa < x <= b:
				#states[state] -= 1
				Change_of_states[state].append(-1)
			elif b < x <= bb:
				#states[state] -= 2
				Change_of_states[state].append(-2)
			elif bb < x <= bbb:
				#states[state] -= 3
				Change_of_states[state].append(-3)
			elif bbb < x <= bbbb:
				#states[state] -= 4
				Change_of_states[state].append(-4)
			elif bbbb < x <= bbbbb:
				#states[state] -= 5
				Change_of_states[state].append(-5)
			elif bbbbb < x <= bbbbbb:
				#states[state] -= 6
				Change_of_states[state].append(-6)
			elif bbbbbb < x <= bbbbbbb:
				#states[state] -= 7
				Change_of_states[state].append(-7)
			elif bbbbbbb < x <= bbbbbbbb:
				#states[state] -= 8
				Change_of_states[state].append(-8)
			elif bbbbbbbb < x <= bbbbbbbbb:
				#states[state] -= 9
				Change_of_states[state].append(-9)
			elif bbbbbbbbb < x <= bbbbbbbbbb:
				#states[state] -= 10
				Change_of_states[state].append(-10)
			elif bbbbbbbbbb < x <= c:
				Change_of_states[state].append(0)
			else:
				print "Unexpected Error."
			simulate_count += 1

states_averaging = {}
for state in states:
	states_averaging[state] = []

def forward_year(year):
	current_year = 1990
	while current_year < year:
		forward_year_probabilities()
		forward_year_values()
		categorise_places(states)
		base_transition_matrix()
		current_year += 1
#	if current_year == year:
	#	difference = states[state] - states_1990[state]
		#states_averaging[state].append(difference)

forward_year(2015)
#final_average_states = {}
#for state in states:
#	final_average_states[state] = numpy.nanmedian(states_averaging[state])
#print str(final_average_states)
print str(states)

#forward_year_values()
#Average_change = {}
#for state in states:
#	Average_change[state] = 0
#for state in Change_of_states:
#	Average_change[state] += numpy.median(Change_of_states[state])

#print str(Average_change)







'''
print "+1:" + str(Chance_of_increasing_by_1)
print "+2:" + str(Chance_of_increasing_by_2)
print "+3:" + str(Chance_of_increasing_by_3)
print "+4:" + str(Chance_of_increasing_by_4)                   #Commented out test that the dictionaries are correctly populated with probabilities
print "+5:" + str(Chance_of_increasing_by_5)
print "-1:" + str(Chance_of_decreasing_by_1)
print "-2:" + str(Chance_of_decreasing_by_2)
print "-3:" + str(Chance_of_decreasing_by_3)
print "-4:" + str(Chance_of_decreasing_by_4)
print "-5:" + str(Chance_of_decreasing_by_5)
'''

'''
a_1990 = str(Chance_of_increasing_by_1)                                          # a = increase ; b = decrease
aa_1990 = str(Chance_of_increasing_by_2)
aaa_1990 = str(Chance_of_increasing_by_3)
aaaa_1990 = str(Chance_of_increasing_by_4)
aaaaa_1990 = str(Chance_of_increasing_by_5)
b_1990 = str(Chance_of_decreasing_by_1)
bb_1990 = str(Chance_of_decreasing_by_2)
bbb_1990 = str(Chance_of_decreasing_by_3)                      #Commented out way to see intial probabilities as of 1990
bbbb_1990 = str(Chance_of_decreasing_by_4)
bbbbb_1990 = str(Chance_of_decreasing_by_5)
f = open("List.txt", "w")
f.write(a_1990 + "\n")
f.write(aa_1990 + "\n")
f.write(aaa_1990 + "\n")
f.write(aaaa_1990 + "\n")
f.write(aaaaa_1990 + "\n")
f.write(b_1990 + "\n")
f.write(bb_1990 + "\n")
f.write(bbb_1990 + "\n")
f.write(bbbb_1990 + "\n")
f.write(bbbbb_1990 + "\n")
f.close()
'''
