# Porject1 Funcs

#porject 1 functions


from math import *

def poundsToKG(pounds):
	kilograms = pounds*0.453592
	return kilograms

def getMassObject (object):
	if object == "t": 
		return 0.1
	elif object == "p":
		return 1.0
	elif object == "r":
		return 3.0
	elif object == "g":
		return 5.3
	elif object == "l":
		return 9.07
	else:
		return 0

def getVelocityObject(distance):
	objVelocity = sqrt(9.8*d/2)
	return objVelocity

def getVelocitySkater(massSkater, MassObject, velObject):
	skatervelocity = massObject*velocitySkater/massSkater
	return skaterVelocity
	

