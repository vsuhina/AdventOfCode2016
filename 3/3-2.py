f = open(r'C:\Users\Vanja\Desktop\AoC2016\3\input.txt','r')

f.seek(0)
lines = f.read().splitlines()

triangles = []

while 1:
	line1 = f.readline()
	if not line1:
		break
	line2 = f.readline()
	line3 = f.readline()
	
	row1 = correct(line1)
	row2 = correct(line2)
	row3 = correct(line3)
	
	triangles.append([row1[0], row2[0], row3[0]])
	triangles.append([row1[1], row2[1], row3[1]])
	triangles.append([row1[2], row2[2], row3[2]])
	

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

def correct(line):
	line = line.replace('\n','')
	sides = line.split(' ')
	sides = list(filter(None, sides))
	return list(map(int, sides))
	