import turtle
input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"
moves = input.split(', ')

pos = [0,0,'N']
turtle.setpos(0,0)
turtle.seth(90)

for move in moves:
	pos = walk(pos, move)
	print(move, ': ', pos)
	
print "Distance: " pos[0] + pos[1]

def walk(pos, move) :
	dist = int(move[1:])
	new_dir = turn(pos[2], move)
	
	if move[0] == 'R' : turtle.rt(90)
	elif move[0] == 'L' : turtle.lt(90)
	turtle.forward(dist * 2)
	
	if (new_dir == 'E') : return [pos[0] + dist, pos[1], new_dir]
	elif (new_dir == 'W') : return [pos[0] - dist, pos[1], new_dir]
	elif (new_dir == 'N') : return [pos[0], pos[1] + dist, new_dir]
	elif (new_dir == 'S') : return [pos[0], pos[1] - dist, new_dir]

def turn(dir, move) :
	turn_right = ['N', 'E', 'S', 'W', 'N']
	turn_left = ['N', 'W', 'S', 'E', 'N']
	turn = []
	
	if (move[0]== 'R') : turn = turn_right
	elif (move[0] == 'L') : turn = turn_left
	
	return turn[turn.index(dir) +1]