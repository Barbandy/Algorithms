import BigInt
import sys
def GCD_bin(a, b):
	if (a < b):
		return GCD_bin(b, a)
	if(b == 0):
		return a
	g = BigInt.BigInt(1)
	while(a % 2 == 0) and (b % 2 == 0):
		a /= 2
		b /= 2
		g *= 2
	while(a != 0):
		while(a % 2 == 0):
			a /= 2
		while(b % 2 == 0):
			b /= 2
		if(a >= b):
			a -= b
		else:
			b -= a
	d = g * b
	return d


print "Euclid's algorithm  GCD_bin(a, b) "
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
if (a < 0) or (b < 0):
	print "a and b must be positive!"
	sys.exit(-1)
print "GCD_bin(", a, ",", b, ") = ", GCD_bin(a,b)