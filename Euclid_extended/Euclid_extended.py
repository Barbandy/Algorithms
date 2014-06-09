import BigInt
import sys
def GCD_ex(a, b):
	if b == 0:
		return a, 1, 0
	if a == 0:
		return b, 1, 0
	
	x1 = BigInt.BigInt(0)
	x2 = BigInt.BigInt(1)
	y1 = BigInt.BigInt(1)
	y2 = BigInt.BigInt(0)
	
	while b != 0:
		q = a / b
		r = a % b
		a = b
		b = r
		
		xx = x2 - x1 * q
		yy = y2 - y1 * q
		x2 = x1
		x1 = xx
		y2 = y1
		y1 = yy
	x = x2
	y = y2

	return a, x, y
	
print "Euclid's algorithm  GCD_ex(a, b) "
print "Enter a:", 
a = BigInt.BigInt(raw_input())
print "Enter b:", 
b = BigInt.BigInt(raw_input())
if (a < 0) or (b < 0):
	print "a and b must be positive!"
	sys.exit(-1)
if a > b:
	GCD, x, y = GCD_ex(a, b)
else:
	GCD, y, x = GCD_ex(b, a)
		
print "GCD_ex (", a, ",", b, ") =", GCD, "=", x, "*", a, "+", y, "*", b  
	
	
	
	
	