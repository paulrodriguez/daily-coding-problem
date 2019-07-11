'''
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
'''


class PrefixMapSum():
	def __init__(self):
		self.keys = {}

	def insert(self,key: str, value: int):
		self.keys[key] = value

	def sum(self,prefix: str):
		s = 0
		for k in self.keys.keys():
			if k.startswith(prefix):
				s += self.keys[k]

		return s


mapsum = PrefixMapSum()

mapsum.insert("columnar",3)
assert mapsum.sum("col") ==3 

mapsum.insert("column",2)
assert mapsum.sum("col") == 5


class Node():
	def __init__(self):
		self.value = 0
		self.sum = 0
		self.children = {}


class PrefixMapSum2():
	def __init__(self):
		self.root = Node()

	def insert(self,key: str,value: int):
		self.insertRec(key,value,0,self.root)

	def insertRec(self,key: str,value: int, pos: int,root: 'Node'):
		if pos==(len(key)-1):
			root.sum -= root.value
			root.value = value
			root.sum += root.value
			return root.sum

		l = key[pos]

		if l not in root.children:
			root.children[l] = Node()

		curr = root.children[l]

		root.sum -= curr.sum

		v = self.insertRec(key,value,pos+1,curr)
		root.sum += v

		return root.sum


	def sum(self,key:str):
		return self.sumRec(key,0,self.root)

	def sumRec(self, key: str, pos: int,root: 'Node'):
		if pos == (len(key)-1):
			return root.sum

		l = key[pos]

		if l not in root.children:
			return 0

		return self.sumRec(key,pos+1,root.children[l])


pms = PrefixMapSum2()

pms.insert('columnar',3)
assert pms.sum('col') == 3
assert pms.sum('cofl') == 0
pms.insert('column',2)
assert pms.sum('col') == 5

pms.insert('column',4)

assert pms.sum('col') == 7

pms.insert('colt',9)

assert pms.sum('col') == 16
