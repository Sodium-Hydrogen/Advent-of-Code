from day3pt1 import numbers

data = [numbers[::],numbers[::]]
for x in range(len(data)):
	for i in range(len(numbers[0])):
		zero = []
		ones = []
		for n in data[x]:
			if n[i] == '0':
				zero.append(n)
			else:
				ones.append(n)
		if len(zero) > len(ones):
			data[x] = zero[::] if x == 0 else ones[::]
		else:
			data[x] = zero[::] if x == 1 else ones[::]
		if len(data[x]) == 1:
			break

print("Oxygen: {}, C02: {}\nTotal: {}".format(
	int("".join(data[0]), 2),
	int("".join(data[1]), 2),
	int("".join(data[0]), 2)*int("".join(data[1]), 2),
))
