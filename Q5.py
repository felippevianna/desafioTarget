string = input("Digite uma string: ")
inversa = ""

for i in range(len(string)-1, -1, -1):
    inversa += string[i]

print("String original: ", string)
print("String invertida: ", inversa)

# OUTRA POSSIBILIDADE DE IMPLEMENTAÇÃO
# # lê a string a ser invertida
# string = input("Digite uma string: ")

# # cria uma lista vazia para armazenar os caracteres invertidos
# chars_invertida = []

# # percorre a string de trás para frente, adicionando cada caractere à lista
# for i in range(len(string)-1, -1, -1):
#     chars_invertida.append(string[i])

# # junta os caracteres invertidos em uma nova string
# string_invertida = ''.join(chars_invertida)

# # imprime a nova string invertida
# print("A string invertida é:", string_invertida)

