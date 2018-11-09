# CS 161 Program Two
# Written by Steven Wilkins
# 26 October 2018
#
# This program asks the user to input the number of 
# cups consumed of both decaf and regular coffee for 
# each hour and calculates the sum at the end of the day.
#
#
# I added a few lines of spacing here and there to make
# the program more readable when it is running. I feel
# like the added breathing room makes it more user friendly.
#
#
#
# This is the revised version that will run on Python 3.




def main( ):
	print("\n\n\n======= R,P,& P DP Dept. Coffee Consumption Report =======\n")
	print("Hour    Regular     Decaf")
	print("------------------------------\n\n")




	totalRegularCups = 0
	totalDecafCups   = 0




	for totalCups in range(1,9):
		regularCups = int(input(
		"Enter the number of cups of regular coffee for hour "
		+str(totalCups) + ": "))

		decafCups = int(input(
		"Enter the number of cups of decaf coffee for hour "
		+str(totalCups) + ": "))




		
		print("\n\n""  " +str(totalCups) + "   \t   " + str(regularCups) 
		+ "   \t      " + str(decafCups) + "\n")

		



		totalRegularCups = float(totalRegularCups + regularCups)

		totalDecafCups = float(totalDecafCups + decafCups)





	totalHours = 8

	averageRegCups = (totalRegularCups / totalHours)

	averageDecafCups = (totalDecafCups / totalHours)




	print("Regular Total: ", totalRegularCups)
	print("\tAverage: ", averageRegCups)
	print("Decaf Total: ", totalDecafCups)
	print("\tAverage: ", averageDecafCups)	
main( )
