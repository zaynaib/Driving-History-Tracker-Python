# Driving History Tracker

This script generates a report containing each driver with total miles driven and average speed. 

## Prerequisite
This program was created using `python 3`.  In order to run it you must have python 3 on your local machine.

## How to run
After downloading app from github.
In the terminal `python cli.py`

## Problem Solving approach

1. ### Choosing a language

One of the first problems that I encountered was deciding what language would be best for solving this challenge. The lanagues that I am most familar with is Javascript and Python. I decided to go with Python because of two reasons.

 1.) Javascript is best used for creating web apps. This challenge is more of a data engineering problem in the sense that I am reading and mainpulating data. Python is more suited for this task.
 
2.) Python has more syntactic sugar that makes it easier to create code.

This challenge would be easier to solve with SQL. I could create a database with two tables driver and trips. These two tables would be join by a primary key of driver id. After joinin the two tables I would implement data aggerations.

2. ### Creating a Plan to create the Solution 

There are two main actions in this problem.

1. Finding the miles per hour for each driver
2. Reading in the input file.

With these two action items I broke the problem into smaller parts.

-------------
**Finding the miles per hour for each driver**

There are two main data models in this challenge which are **Trips** and **Drivers** .
A **Driver** is a person who has at least name, total miles driven, and average miles per hour. 
A **Trip** is a distance and a duration of time (start time, end time).
A **Driver** can take 0 to many trips. 

The best way to represent these two data models is to create objects. Objects make it easy to bundle properties and behavoirs together.



Main behavior functions that the Trip class need to perform.

- Calculate the duration of a time of a trip
- Calculate the miles per hour (mph) of each trip



Main behavior functions that the Driver class needs to perform

- Keep track of all indiviual trips driver has taken
- aggreate total time driven
- aggregate total miles driven
- calculate average speed
- print out results


Trip has 4 properties

- start (string) [Given by input text]
- end (string) [Given by input text]
- distance(Given by intput text)
- minutes(int) [Calcuated by duration function]

Most of these properties were pre determined by the input text that is given from this challenge.

**Minute Property**

I decided to create minutes property for trips because I will need it later when calculating the drivers average speed. 
I used minutes instead of hours because not all trips are going to be in hour intervals. For example Dan total duration is 50 minutes. I could use floats to represent minutes but it would lead to more math conversions. The more math conversions there is more of a chance that I can make an error down the line with calculating mph.  


I did not create miles per hour property because the indiviual trip speed is not needed for final output.


Driver has 4 properties

- name (string) [Name of the Driver]
- user_time(int) [Total time driver has driven]
- user_speed(float) [Miles per hour of the drivers total time driving and total miles traveled]
- total_miles(float) [Total miles driver has driven]
- trips(list) [list of trip instances]

Most of these properties are floats because I wanted to have more precise calculations.
Trips property data structure is a list because I can store multiple objects, add on new trip instances, and delete trip instances. It would not make sense to use a tuple because its immuatble. Which means that we cannot add or edit any trips to the driver. 

### Behavoirs

Duration 

Calculates time difference between a start time and end time. Time is represented by a int. It is not a datetime object because you can't do math with datetime objects and primatives such as ints and floats. I decided to convert the time duration of a trip into minutes because it will make it simpler to calcuate miles per hour. It is easier to divide whole numbers instead of decimals.

speed / avg_speed

calculates miles per hour. The formula for calculate mph is s = d/t. Since time is in minutes instead of hours I mulitpled the mph equation by 60 minutes (d/t) * 60.



**Finding the miles per hour for each driver**

**Reading the input file**

The final half of the solution is reading the input files and calcuating each drivers speed. It can be found in cli.py

I decided to create four functions initDriver and driverTrips, calcTotal,driverOutput. 
initDriver create instances of the Driver class. While driverTrips extracts driver trip information from input text file and adds the information to that particular driver.

**iniDriver** returns a dictionary of drivers. I choose this data structure because it is easier to look up a driver via their name. It is much harder to lookup a specfic driver in a list. In order to do this I would have to know the exact index of the driver.

**driverTrips**
Uses the dictionary created from iniDriver function to loop up a specific driver and add their trips.

**calcTotal** calculates the total distance and time of each driver while driverOutput prints each drivers speed/mileage information.

I know that cli.py does not follow the DRY(Don't Repeat Yourself) paradigm. There are redundancies in my code. But I prefer to follow the single responsbility principal. The single responsbility principal (SRP) states that every method  should have responsibility for just a single task of that program's functionality. It makes it easier to debug and test my code.


**Edge Case**:

An edge case that I did not get the chance to solve is duplicates. If someone has the same name as another person we could create ids. 
Not saving mph as a property for Trip class could be troublesome if further functionality was added in the future. Lets say we want to reimburse a driver based on mph per trip. This would be easier to do if mph was a property.
