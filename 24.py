def inverte(n):
	rev=0
	while(n>0):
		dig=n%10
		rev=rev*10+dig
		n=n//10
	return rev

def isEntirelyOdd(n):
	while(n>0):
		dig=n%10
		if(dig%2==0):
			return False
		n=n//10
	return True

qntd = 0

for n in range (10**9):
	if n%10 == 0: 
		continue

	x = inverte(n)

	candidato = x+n
	if isEntirelyOdd(candidato):
		qntd += 1

print(qntd)