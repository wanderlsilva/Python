nome = input("Digite seu nome completo: ")

if len(nome) > 50: #len() retorna o número de caracteres da string
    print("Seu nome é grande, ele possui mais de 50 letras. ")

print(f"Ele possui {len(nome)} caracteres.")