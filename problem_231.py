'''
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. 
If this is not possible, return None
'''
import heapq

def rearrangeString(s):
	letters = {}
	for ss in s:
		if ss not in letters:
			letters[ss] = 0
		letters[ss] += 1

	m = 0
	
	arr = []

	for l in letters:
		arr.append((letters[l],l))
		if letters[l] > m:
			m = letters[l]

	if (m-1) > (len(s)-m):
		return None

	res = ""

	heap = []
	for l in letters:
		heapq.heappush(heap,(-letters[l],l))

	while len(heap) > 0:
		t,l = heapq.heappop(heap)
		if len(res) > 0 and res[-1] == l:
			t2,l2 = heapq.heappop(heap)
			res += l2
			letters[l2] -= 1
			if letters[l2] > 0:
				heapq.heappush(heap,(-letters[l2],l2))
		res += l
		letters[l] -= 1
		if letters[l] > 0:
			heapq.heappush(heap,(-letters[l],l))


	return res
print(rearrangeString("aaabbc"))
print(rearrangeString("aaac"))
print(rearrangeString("aaacder"))
print(rearrangeString("aaacd"))

print(rearrangeString("aaac"))
	
