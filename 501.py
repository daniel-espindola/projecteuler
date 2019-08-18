primos = open("cousins.txt",'r')

primos = primos.read()
primos = primos.replace("\n", "")

primos = primos.split(" ")

primos = [int(n) for n in primos if n!=""]
print(primos)