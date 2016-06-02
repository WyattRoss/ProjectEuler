file = open("Numbers.txt", "r")
content = ""
for i in file:
	content += i
content = content.split("\n")
total = ""
for i in content:
	total += i
	total += " "
totals = total.split(" ")
totalF = 0
nums = 0
for i in xrange(len(totals)-1):
	totalF += int(totals[i])
	nums += 1
print totalF, nums
