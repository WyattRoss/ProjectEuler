from Prime_Gen import *
candidate = 1
pNum = 0
while 1:
	if is_prime(candidate) == True:
		pNum += 1
		if pNum == 10001:
			print candidate
			break
	candidate += 2