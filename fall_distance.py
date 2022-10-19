#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 10/19/2022
#This code contains a function definition for distance an object has fallen.

#distance fallen equation is d=(1/2)gt^2

#define variables: g=gravity in m/s^2, t is time the object has been falling, and dist is the result of d when all values have been entered

#define variable for time_fall in definition (time_fall is user's input squared)
def fall_distance(t):
    g=9.8
    d=((1/2)*g*(t**2))
    return (d)
#below is the print test i ran to ensure code ran
dist=fall_distance(4.5)
#print(dist)
#it printed 99.225