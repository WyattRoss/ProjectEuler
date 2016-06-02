import numpy as np
""" notation is 2dArray[row][collumn]"""
def GoDiagLToR(twoDarray):
	nums = []
	col = 0
	for row in range(len(twoDarray)):
		nums.append(twoDarray[row][col])
		col += 1
	return nums
def GoDiagRToL(twoDarray):
	nums = []
	col = len(twoDarray[1])-1
	for row in range(len(twoDarray)):
		nums.append(twoDarray[row][col])
		col -= 1
	return nums
def GoDiagRL(twoDarray, StartRow):
	sets = []
	nums = []
	StartRow -= 1
	row = StartRow
	col = len(twoDarray) - 1
	for row in xrange(StartRow, len(twoDarray)-1):
		nums.append(twoDarray[row][col])
		col -= 1
	sets.append(nums)
	nums = []
	col = len(twoDarray) - 1
	for row in xrange(StartRow+1, -1, -1):
		nums.append(twoDarray[row][col])
		col -= 1
	sets.append(nums)
	return sets
def GoDiagLR(twoDarray, StartRow):
	sets = []
	nums = []
	StartRow -= 1
	row = StartRow
	col = 0
	for row in xrange(StartRow, len(twoDarray)-1):
		nums.append(twoDarray[row][col])
		col += 1
	sets.append(nums)
	nums = []
	col = 0
	for row in xrange(StartRow+1, -1, -1):
		nums.append(twoDarray[row][col])
		col += 1
	sets.append(nums)
	return sets
def GoVert(twoDarry, col):
	nums = []
	for i in range(0, len(twoDarry)):
		nums.append(twoDarry[i][col-1])
	return nums
def GoHorz(twoDarry, row):
	nums = []
	for i in twoDarry[row-1]:
		nums.append(i)
	return nums
def sumList(lst):
	return sum(lst)
def calcList(lst):
	total = 1
	for i in lst:
		total *= i
	return total