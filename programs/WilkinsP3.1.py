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
	highest = 0.0
	count = 0


	while employeeName != "DOA":


		amount = float(input("Enter amount collected by " \
		+ employeeName + ": "))

		count = count + 1

		if count == 1:
			lowest = amount

		if amount >= highest:
			winner = employeeName
			highest = amount

		if amount <= lowest:
			loser = employeeName
			lowest = amount

		employeeName = input("Enter name of next associate: ")


	print("The winner is", winner, "who collected $", highest, "in premiums!")
	print("The loser is", loser, "who only collected $", lowest, "in premiums!")


main ( )

