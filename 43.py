import math
import random

def digita(n):
    return [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]

def pandigital(digits):
    res = ""
    while(digits != []):
        a = digits[random.randint(0,len(digits)-1)]
        res += str(a)
        digits.remove(a)
    return int(res)
        
pand = {}
length = 0

while length <362880:
    
    digits = [1,2,3,4,5]
    a = pandigital(digits)
    res = ""

    for i,digit in enumerate(str(a)):
        if(i==4):
            res+= '0'
        res+=digit
    
    length = len(pand)
    print(length)
    pand[int(res)] = 1

res = open("pandi.txt",'w')
res.write((str(pand.keys())))

print(len(pand))