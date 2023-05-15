n = int(input('Enter number por favor:'))
sum = 0
def sum_mult3_5(n):
	global sum
	for i in range(1, n + 1):
		if i % 3 and i % 5 == 0:
			sum += i
		elif i % 3 == 0:
			sum += i
		elif i % 5 == 0:
			sum += i

sum_mult3_5(n)
print(sum)

# not getting expected value