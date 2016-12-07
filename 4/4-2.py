import re

f = open(r'C:\Users\Vanja\Desktop\AoC2016\4\input.txt','r')

f.seek(0)
lines = f.read().splitlines()

pattern = '([a-z\-]+)(\d+)\[([a-z]+)\]'


for line in lines:
	m = re.search(pattern, line)
	elements = list(m.groups())
	
	code = elements[0].replace('-','')
	nameEnc = elements[0]
	id = (int)(elements[1])
	checksum = elements[2]
	
	if isValid(code, checksum):
		name = decrypt(nameEnc, id)
		print (name, id)
	
def isValid(code, checksum):
	charCount = []
	chars = list(set(code))
	chars.sort()
	for c in chars:
		charCount.append([c,code.count(c)])
		
	charCount.sort(key= lambda x: (-x[1], x[0]))
	
	for i in range(0,5):
		if (charCount[i][0] != checksum[i]):			
			return False
					
	return True
	
def decrypt(code, id):
	return code
	