'''
Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. 
On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. 
If they land on a square that represents a snake or ladder, 
they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.
'''
from collections import defaultdict

def minTurns(snakes,ladders):
	curr, moves = 0,0
	visited = defaultdict(bool)
	o = []
	return dfs(snakes,ladders,curr,moves,visited,o)

def dfs(snakes,ladders,curr,moves,visited,o):
	#print(curr)
	if curr == 100:
		#print('moves',moves)
		#print(o)
		return moves

	if curr in snakes:
		curr = snakes[curr]
		if visited[curr] == True:
			return float('inf')

	if curr in ladders:
		curr = ladders[curr]
		if visited[curr] == True:
			return float('inf')
	
	visited[curr] = True
	best = float('inf')
	for i in range(1,7):
		n  = curr + i
		#print(curr,i,(curr+i),o,visited[n])
		if visited[n] == True or n > 100:
			#print('have visited',n)
			continue

		
		#visited[n] = True
		o.append(curr+i)
		best = min(best,dfs(snakes,ladders,curr+i,moves+1,visited,o))
		o.pop()
		#visited[n] = False
	visited[curr] = False
	return best

snakes  = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

print(minTurns(snakes,ladders))
