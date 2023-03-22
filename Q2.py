# lê um número do usuário
num = int(input("Digite um número: "))

# inicializa as variáveis para os 2 primeiros valores da sequência
fib1 = 0
fib2 = 1

# loop para calcular os próximos valores da sequência até que o valor seja maior ou igual ao número informado
while fib2 < num:
    # calcula o próximo valor da sequência
    fib3 = fib1 + fib2
    # atualiza as variáveis para o próximo cálculo
    fib1 = fib2
    fib2 = fib3

# verifica se o número informado pertence à sequência
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci!")
else:
    print(num, "não pertence à sequência de Fibonacci.")

# OUTRA SOLUÇÃO POSSIVEL

# # define a função que calcula a sequência de Fibonacci até o número informado
# def fibonacci(n):
#     # inicia a sequência com os valores iniciais 0 e 1
#     sequencia = [0, 1]
    
#     # adiciona os próximos valores da sequência até atingir ou ultrapassar o número informado
#     while sequencia[-1] < n:
#         prox_valor = sequencia[-1] + sequencia[-2]
#         sequencia.append(prox_valor)
    
#     # verifica se o número informado pertence à sequência
#     if n in sequencia:
#         print(f"O número {n} pertence à sequência de Fibonacci: {sequencia}")
#     else:
#         print(f"O número {n} não pertence à sequência de Fibonacci: {sequencia}")

# # chama a função e informa o número a ser verificado
# fibonacci(21)
