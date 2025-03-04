n = int(input('Digite um número: '))
soma = 0
potencia = 0
algarismo = 0
while n//(10**potencia) != 0:
    algarismo = (n//(10**potencia))%10
    soma += algarismo
    potencia+=1
print(f'{soma}')