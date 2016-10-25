# 1) Você é o mais novo analista da National Security Agency – NSA, a agência de segurança norte-americana.
# Como primeira tarefa você foi designado para desenvolver um sistema que cadastre a senha de 4 (quatro) usuários em uma matriz 2x2.
# Em seguida, o programa deverá solicitar ao usuário sua senha.
# Caso a senha digitada esteja cadastrada na matriz de senhas, o programa deverá exibir a mensagem “Bem vindo!”.
# Caso contrário, deverá exibir a frase “Usuário não cadastrado”.



# senhas = [[input('Senha a ser cadastrada: '),
#            input('Senha a ser cadastrada: ')],
#           [input('Senha a ser cadastrada: '),
#            input('Senha a ser cadastrada: ')]]
#
#
# for linha in senhas:
#     for elemento in linha:
#         print(senhas)
#
# usuarioSenha = input('Digite sua Senha: ')
#
# for linha in senhas:
#     for usuarioSenha in linha:
#         if usuarioSenha == elemento:
#             print('Seja bem vindo!')
#         else:
#             print('Senha não cadastrada!')




# 2) Faça um programa que represente a matriz 3x2 abaixo e calcule e exibe a
# quantidade de números negativos, a soma dos números positivos dessa mesma matriz,
# a quantidade de números ímpares e a quantidade de números pares.

# matriz = [[int(input('Digite o 1º número: ')),int(input('Digite o 2º número: '))],
#           [int(input('Digite o 3º número: ')),int(input('Digite o 4º número: '))],
#           [int(input('Digite o 5º número: ')),int(input('Digite o 6º número: '))]]
#
# contador_numero_negativo = 0
# soma_positivos = 0
# contador_numero_impar = 0
# contador_numero_par = 0
#
# for linhas in matriz:
#     for numero in linhas:
#         if numero < 0:
#             contador_numero_negativo = contador_numero_negativo + 1
#         else:
#             soma_positivos = soma_positivos + numero
#         if numero % 2 == 0:
#             contador_numero_par = contador_numero_par + 1
#         else:
#             contador_numero_impar = contador_numero_impar + 1
#
# print('Números negativos: ', contador_numero_negativo)
# print('A soma dos números positivos: ', soma_positivos)
# print('Números ímpares:', contador_numero_impar)
# print('Números pares:', contador_numero_par)
# print('Os números digitados foram: ',matriz)



# 3) Para um sistema de Recursos Humanos, descubra qual o maior salário da empresa.
# Todos os salários foram armazenados em uma matriz 3x3 composta assim, por 9 (nove) salários dos funcionários da empresa.
# Todos os salários devem ser fornecidos pelo chefe do departamento de RH da empresa.


# salarios = [[float(input('Qual  sálario do 1º funcinário: ')),
#              float(input('Qual  sálario do 2º funcinário: ')),
#              float(input('Qual  sálario do 3º funcinário: '))],
#             [float(input('Qual  sálario do 4º funcinário: ')),
#              float(input('Qual  sálario do 5º funcinário: ')),
#              float(input('Qual  sálario do 6º funcinário: '))],
#             [float(input('Qual  sálario do 7º funcinário: ')),
#              float(input('Qual  sálario do 8º funcinário: ')),
#              float(input('Qual  sálario do 9º funcinário: '))]]
#
#
# maior = 0
#
#
# for linha in salarios:
#     for salario in linha:
#         if salario > maior:
#             maior = salario
#
# print('O maior Salário eh: ', maior)
