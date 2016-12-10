f = open(r'C:\Users\Vanja\Desktop\AoC2016\7\input.txt','r')

lines = f.read().splitlines()

pattern_brackets = '\[[a-z]+\]'

results = []

for line in lines:
	ABAs = checkABA(outside(line))
	BABs = checkABA(''.join(inside(line)))
	
	for aba in ABAs:
		bab = transform(aba)
		if bab in BABs:
			results.append(line)
			break

len(results)

def transform(str):
	return ''.join([str[1], str[0], str[1]])

def inside(str):
	return re.findall(pattern_brackets, str)

def outside(str):
	brackets = inside(str)
	for br in brackets:
		str = str.replace(br,'[]')		
	return str
	
def checkABA(str):
	res = []
	l = list(str)
	for i in range(0, len(str)-2):
		segment = l[i:i+3]		
		rev_segment = list(reversed(segment))				
		if ''.join(segment) == ''.join(rev_segment):
			if ((l[i] == l[i+1])):			
				continue
			res.append(''.join(segment))			
	return res
