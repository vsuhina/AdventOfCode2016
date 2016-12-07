import hashlib

inputStr = "ugkcyxxp"

count = 0
password = ['','','','','','','','']

for i in range(0,100000000):
	byteInput = bytes(inputStr + str(i), 'ascii')
	h = hashlib.md5(byteInput).hexdigest()
	if (h[0:5] == '00000'):
		pos = h[5]
		if pos >= '0' and pos <= '7':
			pos = int(pos)
			if (password[pos] == ''):
				password[pos] = h[6]
				print(h, h[5], h[6])
				count += 1
				if (count == 8):
					break
				
print(''.join(password))
