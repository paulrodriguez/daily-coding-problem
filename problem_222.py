'''
Given an absolute pathname that may have . or .. as part of it, 
return the shortest standardized path.
'''

def shortestStandardizedPath(path):
	folders = path.split('/')

	res = []

	for f in folders:
		if f == '.':
			continue
		elif f == '..':
			if len(res) > 0:
				res.pop()
			

		else:
			if f != '':
				res.append(f)

	if len(res) == 0:
		return '/'

	return ('/'+'/'.join(res)+'/')


print(shortestStandardizedPath('/usr/bin/../bin/./scripts/../'))
print(shortestStandardizedPath('/./././././usr/bin/../bin/./scripts/../'))
print(shortestStandardizedPath('/../usr/bin/../bin/./scripts/../'))
print(shortestStandardizedPath('/a/./'))
print(shortestStandardizedPath('/a/b/..'))
print(shortestStandardizedPath('////'))
print(shortestStandardizedPath('/home/'))
print(shortestStandardizedPath('/a/./b/../../c/'))
print(shortestStandardizedPath('/a/../'))
print(shortestStandardizedPath('/../../../../../a/'))
print(shortestStandardizedPath('/a/./b/./c/./d/'))
print(shortestStandardizedPath('/a/../.././../.././'))
print(shortestStandardizedPath('/a//b//c//////d/'))
