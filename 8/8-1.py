import re

f = open(r'C:\Users\Vanja\Desktop\AoC2016\8\input.txt','r')

lines = f.read().splitlines()

pattern_rect = 'rect (\d+)x(\d+)'
pattern_rotate_row = 'rotate row y=(\d+) by (\d+)'
pattern_rotate_col = 'rotate column x=(\d+) by (\d+)'

patterns = [pattern_rect, pattern_rotate_col, pattern_rotate_row]

screen_width = 50
screen_height = 6

screen = createScreen(screen_width, screen_height)

for line in lines:
	for p in patterns:
		m = re.match(p, line)
		if m != None:
			params = m.groups()
			if p == pattern_rect:
				drawRect(int(params[0]), int(params[1]))
				break
			elif p == pattern_rotate_col:
				drawRotateCol(int(params[0]), int(params[1]))
				break
			elif p == pattern_rotate_row:
				drawRotateRow(int(params[0]), int(params[1]))
				break
	print(line)
	input("Press Enter to continue...")
	print(' ')
	draw(screen)
				
				
def drawRect(wide, tall):
	for i in range(0,tall):		
		for j in range(0,wide):
			screen[i][j] = '#'	
	
def drawRotateCol(x, offset):
	for i in range(0, offset):
		last = screen[screen_height-1][x]
		r = list(range(0, screen_height))
		r.reverse()
		r.remove(0)
		for row in r:
			screen[row][x] = screen[row-1][x]
		screen[0][x] = last		
	
def drawRotateRow(y, offset):	
	for i in range(0, offset):
		last = screen[y][screen_width-1]
		r = list(range(0, screen_width))
		r.reverse()
		r.remove(0)
		for col in r:
			screen[y][col] = screen[y][col-1]
		screen[y][0] = last
	
def createScreen(width, height):
	screen = []
	for i in range(0, height):
		row = ['.'] * width
		screen.append(row)
	return screen
	
def draw(screen):
	for row in screen:
		print (''.join(row))
		
def countPixels(screen):
	count = 0
	for row in screen:
		count += row.count('#')
	return count
