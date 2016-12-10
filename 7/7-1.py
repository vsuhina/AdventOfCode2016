f = open(r'C:\Users\Vanja\Desktop\AoC2016\7\input.txt','r')

lines = f.read().splitlines()

pattern_brackets = '\[[a-z]+\]'

results = []

for line in lines:
	brackets = re.findall(pattern_brackets, line)
	isABBAinBracket = False
	for el in brackets:
		if (checkABBA(el)):
			isABBAinBracket = True
			break
						
	if (not(isABBAinBracket) and checkABBA(line)):
		results.append(line)

len(results)
	
def checkABBA(str):
	l = list(str)
	for i in range(0, len(str)-3):
		segment = l[i:i+4]		
		rev_segment = list(reversed(segment))				
		if ''.join(segment) == ''.join(rev_segment):
			if ((l[i] == l[i+1]) or (l[i+2] == l[i+3])):			
				continue
			print(segment, str)
			return True
	return False
