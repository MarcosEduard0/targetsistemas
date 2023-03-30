string = "Gostaria de estagiar na Target Sistemas"  # string a ser invertida
invertida = ""  # string vazia que irá armazenar a string invertida

# percorre a string de trás para frente, adicionando cada caractere na string invertida
for i in range(len(string)-1, -1, -1):
    invertida += string[i]

# imprime a string invertida
print(invertida)
