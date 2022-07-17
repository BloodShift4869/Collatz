import time
import math

# Test if number is even
def isEven(num):
	if num % 2 == 0:
		return True
	else:
		return False

# Test if numbers are coprime
def isCoprime(a, b):
	return math.gcd(int(a), int(b)) == 1

# Collatz algorithm
def collatz(number):
	result = []
	result.append(number)

	while number != 1:
		if isEven(number):
			number /= 2
		else:
			number = number * 3 + 1

		result.append(number)

	length = len(result)
	digitSum = sum(result)

	if isCoprime(length, digitSum) == False:
    return 0 
	else:
		return 1 

# Get user input
number = int(input("Geben Sie eine Zahl groesser Null ein: "))

# Test if number is in allowed range (greater than zero)
if number <= 0:
  print("Die eingegebene Zahl war kleiner oder gleich Null.")
  exit()

# Iterate through all numbers from 1 to n
n = number
isNotCoprime = 0

start = time.time()

while n != 0:
	isNotCoprime += collatz(n)
	n -= 1

pi = math.sqrt(6 / (isNotCoprime / number))

end = time.time()

print("Annaeherung an Pi: " +str(pi))
print("Berechnungsdauer: " +str(end - start) +" ms.")
