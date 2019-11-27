# Driving History Tracker

## Problem Solving approach

1. ### Choosing a language

One of the first problems that I encountered was deciding what language would be best for solving this challenge. The lanagues that I am most familar with is Javascript and Python. I decided to go with Python because of two reasons. 1.) Javascript is best used for creating web apps. This challenge is more of a data engineering problem in the sense that I am reading and mainpulating data. Python is more suited for this task. 2.) Python has more syntactic sugar that makes it easier to create code.

2. ### Creating a Plan to create the Solution 

There are two main actions in this problem.

1. Finding the miles per hour for each driver
2. Reading in the input file.

With these two action items I breaking the problem into smaller parts.

**Finding the miles per hour for each driver**

Based on the challenge prompt a driver will have at least three properties a name, miles driven, and miles per hour. The best data structure to represent an indiviual driver is an object. Objects make it easy to create to bundle properites nd behaviors together.

The Driver class is a blueprint for each driver.

Main functions that the Driver class needs to perform

- time difference
- aggreate total time of driver
- calculate speed (miles per hour)
- aggregate total time miles

It has 4 properties

- name (string) [Name of the Driver]
- user_time(float) [Total time driver has driven]
- user_speed(float) [Miles per hour of the drivers total time driving and total miles traveled]

- total_miles(float) [Total miles driver has driven]

Most of these proprties are floats because
Time is a float in order to account for hours and minutes.
Miles is float instead of an int because we want to have more precise calculations.

### Behavoirs

diff
Calculates time difference between a start time and end time. Time is represented by a float. I represented time as a float instead of int because of hours and minutes. It is not a datetime object because you can't do math with datetime objects and primatives such as ints and floats.

speed

calculates miles per hour. he formula for calculate mph is s = d/t . This formula usually works unless the drivers time is less thatn 1 hour. If this is the case I have divide (60 minutes/ x minutes) * miles driven in order to find miles per hour. 
This function returns a float that is rounded by 2 decimal places. It makes it easier to test.


miles
Miles function keeps track of the number of miles.

print_out
Print out functions return the string the desired output for this challenge
Name_driver: x miles driven @ x mph


**Finding the miles per hour for each driver**

**Reading the input file**

For the final half of the solution is reading the input files and calcuating each drivers speed. It can be found in cli.py

I decided to create two functions initDriver and driverInfo. 
initDriver create instances of the Driver class. While driverInfo calcuates the driver's information such as total miles, total time, and miles per hour.

iniDriver returns a dictionary of drivers. I choose this data structure because it is easier to look up a driver via their name. It is much harder to lookup a specfic driver in a list. In order to do this I would have to know the exact index of the driver. 

I know that cli.py does not follow the DRY(Don't Repeat Yourself) paradigm. There is some redundancies in my code. But I have these two functions in order to folow the single responsbility principal. Each method has a single task to carry out. It made it easier for me to test my code.

**Edge Case**:

An edge case that I did not get the chance to solve is duplicates. If someone has the same name as another person we could create ids. 