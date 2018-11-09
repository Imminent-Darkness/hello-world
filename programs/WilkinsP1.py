# CS 161 Program One
# Written by Steven Wilkins
# 11 October 2018
#
# This program inputs a base value and shows the first eight powers of that base.

def main ( ):
	base = input ("Please enter the base value: ")
	base = int (base)
	power = base	
	exponent = 1
	power = base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
	exponent = exponent + 1
	power = power * base
	print (base, "to the", exponent, "power is", power, ".")
main ( )
