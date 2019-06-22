'''
Given a string of digits, generate all possible valid IP address combinations.
'''

def generateIps(s):
	return util(0,s,0,"",[])

def util(start,s,n,ss,res):
	#print(start,ss)
	if start == len(s):
		#print('reached end',ss)
		if n == 4:
			res.append(ss[1:])
		return res

	if (len(s)-1 - start) < (4-n) or (len(s)-1-start) > (4-n)*3:
		return res
	
	if int(s[start]) >= 3:
		for i in range(start,min(len(s),start+2)):
			tmp = ss+'.'+s[start:i+1]
			res= util(i+1,s,n+1,tmp,res)

		return res

	if s[start] == '0':
		return util(start+1,s,n+1,ss+"."+s[start],res)

	if s[start] == '1':
		for i in range(start, min(len(s),start+3)):
			#print('i at ',i,ss+'.'+s[start:i+1])
			tmp = ss+'.'+s[start:i+1]
			res = util(i+1,s,n+1,tmp,res)

		return res

	if s[start] == '2':
		m = min(len(s),start+1)
		if (start+1) < len(s):
			if int(s[start+1])== 5:
				if (start+2)< len(s) and int(s[start+2]) <= 5:
					m = min(len(s),start+3)
				else:
					m = min(len(s),start+2)
			elif int(s[start+1]) < 5:
				m = min(len(s), start+3)
		#print(m)
		for i in range(start,m):
			#print('2 i at ',i,ss+"."+s[start:i+1])
			res = util(i+1,s,n+1,ss+"."+s[start:i+1],res)


	return res



			
print(generateIps('2542540123'))			
print(generateIps('255255255255'))			
