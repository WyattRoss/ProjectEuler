i = 20
def is1T20(i):
	for b in xrange(1, 21):
		if i % b != 0:
			return False
	return True
while 1:
	if is1T20(i) == True:
		print i
		break
	i += 20