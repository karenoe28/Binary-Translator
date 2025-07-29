textito = input("Ingresa tu texto: ")
binarios = []

for letrita in textito:
    ascii_num = ord(letra)
    bin_8bits = format(ascii_num, "08b")
    binarios.append(bin_8bits)

binario_final = ""
for x in binarios:
    binario_final += x + " "
binario_final = binario_final.strip()

print(binario_final)
