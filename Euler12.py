import TriTypeSets

def divisorCount(N):
    return len([x for x in range(1,N/2) if not divmod(N,x)[1]])
TriNumber = 1500
while 1:
	c = TriTypeSets.nthTri(TriNumber)
	if divisorCount(c) > 500:
		print c
		break
	TriNumber += 1
	print divisorCount(c)