f = open(r'C:\Users\Vanja\Desktop\AoC2016\6\input.txt','r')

lines = f.read().splitlines()
matrix = list(map(list, lines))
transposed = list(zip(*matrix))

for row in transposed:
	print(min(set(row), key=row.count))
