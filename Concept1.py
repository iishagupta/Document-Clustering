import math
def getTreailingZeroes(inString):
	return (len(inString)-len(inString.rstrip('0')))

for x in range(402,700):
	print(x,"->", getTreailingZeroes(str(math.factorial(x))))