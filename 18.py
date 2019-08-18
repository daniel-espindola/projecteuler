import functools

#@functools.lru_cache(maxsize=128, typed=False)
def maxpath(row=0, column=0):
	if(row==len(triangle)-1):
		return triangle[row][column]

	#ir pra esquerda vs ir pra direita
	left = maxpath(row+1, column)
	right = maxpath(row+1, column+1)

	return max(left,right) + triangle[row][column]

file = open('p067_triangle.txt','r')
triangle = file.read()
aux = []

##transforma o texto em uma matriz
aux = triangle.split('\n')
aux = [line.split(' ') for line in aux]

#converte essa bosta em inteiros
triangle=[]
i=j=0

while (i<len(aux)):
	triangle.append([])
	j=0
	while(j<len(aux[i])):
		triangle[i].append(int(aux[i][j]))
		j+=1
	i+=1


print(maxpath(0,0))