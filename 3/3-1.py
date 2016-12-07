f = open(r'C:\Users\Vanja\Desktop\AoC2016\3\input.txt','r')

f.seek(0)
lines = f.read().splitlines()

triangles = []

for line in lines:
	sides = line.split(' ')
	sides = list(filter(None, sides))
	triangles.append(list(map(int, sides)))
	
possibleCount = 0

for tr in triangles:
	tr.sort()
	if (tr[0] + tr[1] > tr[2]):
		possibleCount += 1
		
print(possibleCount)