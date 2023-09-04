def valor(n):
    return dobro_elevado_a_n(n)

def dobro_elevado_a_n(x):
    resultado = (x*2)**x
    return print(resultado)

num = int(input('Digite um número inteiro: '))
valor(num)