import BigInt
import sys
def GCD(a, b):
	if (a < b):
		return GCD (b, a)
	if b == 0:
		return a
	r = 1
	while r != 0:
		r = a % b
		a = b
		b = r
	return a
	
print "Euclid's algorithm  GCD(a, b) "
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
if (a < 0) or (b < 0):
	print "a and b must be positive!"
	sys.exit(-1)
print "GCD(", a, ",", b, ") = ", GCD(a,b)
	
	
	
	
	