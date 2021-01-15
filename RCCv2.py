#!/usr/bin/python

print("Welcome to the Rayburn Cable Calculator!(RCC)") #This will print the welcome message
comp = raw_input("What is your company name?") #This will prompt for the company name
feet = float(input("How many feet of cable do you need?")) #This will prompt for the feet of cable needed

if feet > 100 and feet < 250:
	math = feet * .80 #This is math
	print('To install {0} ft of cable, {1} will spend ${2}'.format(feet,comp,math)) #This will print the required information

elif feet > 250 and feet < 500:
	math1 = feet * .70 #This is math
	print('To install {0} ft of cable, {1} will spend ${2}'.format(feet,comp,math1)) #This will print the required information

elif feet > 500:
	math2 = feet * .50 #This is math
	print('To install {0} ft of cable, {1} will spend ${2}'.format(feet,comp,math2)) #This will print the required information

else:
	math3 = feet * .87 #This is math
	print('To install {0} ft of cable, {1} will spend ${2}'.format(feet,comp,math3)) #This will print the required information