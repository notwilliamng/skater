# Project 1
#
# Name: William Ng
# Instructor: Workman
# Section: 03

from funcs.py import *

def main():
	weight = float (input("How much do you weigh (pounds)? "))
	dist = float (input("How faw away is your professor (meters)? "))
	object = input ("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? " )

    print("Nice Throw!")
    kg = poundsToKg(weight)
    mass = getMassObject(object)
    velocity = getVelocityObject(dist)
    skater_velocity = getVelocitySkater(weight,object,velocity)

    if mass <= 0.1:
        print("You're going to get an F")
    elif mass > 0.1 and mass <= 1.0:
        print("Make sure your professor is OK.")
    elif mass > 1:
        if dist < 20:
            print("How far is the hospital?")
        else:
            print ("RIP Professor")
    if velocity < 0.2:
        print("My grandmother skates faster than you!")
    elif velocity >= 0.2 and < 1.0:
        pass
    else velocity >= 1.0:
        print("Look out for that railing!!!")

if __name--=='__main__' :
	main()	
