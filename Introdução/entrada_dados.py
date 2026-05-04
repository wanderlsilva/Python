#FUNÇÃO INPUT
nome = input("Digite seu nome: ")

#É importante destacar que a função input() sempre retornará o valor recebido no formato de uma string

idade = input("Digite sua idade: ")
print(type(idade)) #Está retornando STRING

idade = int(input("Informe sua idade: "))
print(idade) #Agora está retornando numero INTEIRO

#ENCONTRO O ERRO
base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))
area = base * altura
print(area)