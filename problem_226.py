'''
You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.
'''

def alienDictionary(words):
	degrees = {}
	graph = {}

	for i in range(len(words)-1):
		for j in range(i+1,len(words)):
			x = 0
			y = 0
			while x < len(words[i]) and y < len(words[j]) and words[i][x] == words[j][y]:
				x += 1
				y += 1

			if x == len(words[i]):
				for l in words[j]:
					if l not in degrees:
						degrees[l] = 0
					if l not in graph:
						graph[l] = set()

			elif y == len(words[j]):
				for l in words[i]:
					if l not in degrees:
						degrees[l] = 0
					if l not in graph:
						graph[l] = set()

			else:
				l = words[i][x]
				ll = words[j][y]
				if l not in degrees:
					degrees[l] = 0
				if l not in graph:
					graph[l] = set()
				
				skip = True if ll in graph[l] else False

				graph[l].add(ll)
				
				if ll not in degrees:
					degrees[ll] = 0

				if skip == False:
					degrees[ll] += 1

	total_letters = len(degrees.keys())
	queue = []
	for l in degrees:
		if degrees[l] == 0:
			queue.append(l)
		
	res = []
	while len(queue) > 0:
		tmp_queue = []
		for l in queue:
			res.append(l)
			if l in graph:
				for ll in graph[l]:
					degrees[ll] -= 1
					if degrees[ll] == 0:
						tmp_queue.append(ll)

		queue = tmp_queue

	if total_letters!=len(res):
		return "invalid"
	return ''.join(res)


print(alienDictionary(['x','xy','zx']))		
print(alienDictionary(['x','y','x']))
print(alienDictionary(['wrt','wrf','er','ett','rftt']))
print(alienDictionary(["dvpzu","bq","lwp","akiljwjdu","vnkauhh","ogjgdsfk","tnkmxnj","uvwa","zfe","dvgghw","yeyruhev","xymbbvo","m","n"]))
print(alienDictionary(["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]))
