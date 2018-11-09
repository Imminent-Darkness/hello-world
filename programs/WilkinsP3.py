# CS 161 Program Three
# Written by Steve Wilkins
# 09 November 2018
#
# This program collects the data from an insurance
# company and delivers a report on who collected the
# most money and who collected the least.


def main ( ):


	employeeName = input("Enter name of next associate: ")
	winner = employeeName
	loser = employeeName
	highest = 0.00
	totalCollections = 0.00
	count = 0.00
	report = "==== The Family Insurance Winner and Loser Report ====\n\n"


	while employeeName != "DOA":

		amount = float(input("Enter amount collected by " \
		+ employeeName + ": "))

		totalCollections = totalCollections + amount

		count = count + 1

		report = (report + employeeName + "\t\t$" + str(amount) + "\n")

		if count == 1:
			lowest = amount

		if amount >= highest:
			winner = employeeName
			highest = amount

		if amount <= lowest:
			loser = employeeName
			lowest = amount

		employeeName = input("Enter name of next associate: ")

	average = round(float(totalCollections/count),2)

	for blank in range (25):
		print("\n")


	report = (report + "\n\nTotal\nCollections:\t$" \
	+ str(totalCollections) + "\nAverage\t\t$" + str(average) \
	+ "\n\nThe winner is " + winner + " who collected $" + str(highest) \
	+ " in premiums!\n" + "The loser is " + loser + " who only collected $" \
	+ str(lowest) + " in premiums!")

	print(report)


	if lowest >= (.2 * highest):
		print("\t--We hope he does better next time..\n\n\n")
	else:
		print("\n\tWe'll miss him!\n\n\n")


main ( )

