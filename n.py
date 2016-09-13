#FizzBuzz


n = 1
while n <= 100:
	if (n % 3 == 0) and (n % 5 == 0):
		print "FizzBuzz"
	if n % 3 == 0:
		print "Fizz"
	if n % 5 == 0:
		print "Buzz"
	else: 
		print str(n)
	n = n + 1

