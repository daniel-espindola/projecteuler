import functools
res = 0

@functools.lru_cache()
def facto(num): 
    if num == 1 or num==0: 
        return 1
    else: 
        return num * facto(num-1) 

for i in range(3,300000):
    soma = 0
    teste = [int(d) for d in str(i)]
    for digit in teste:
        soma += facto(digit)

    if soma == i:
        res += i
print(res)