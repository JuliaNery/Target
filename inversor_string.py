string = input("Insira a palavra: \n")
print(string)

num_caracteres = len(string) - 1
inverso = ""

while num_caracteres >= 0:
    inverso = inverso + string[num_caracteres]
    num_caracteres -= 1
print(inverso)
