import hashlib

inputStr = "ugkcyxxp"

count = 0

for i in range(0,100000000):
	byteInput = bytes(inputStr + str(i), 'ascii')
	h = hashlib.md5(byteInput).hexdigest()
	if (h[0:5] == '00000'):
		print(h, h[5])
		count += 1
		if (count == 8):
			break
