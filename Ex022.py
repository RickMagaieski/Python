nome = str(input("Digite seu nome completo: ")).strip()
separado = nome.split()
print(f"O seu nome em letras maiúsculas fica assim: {nome.upper()}")
print(f"O seu nome em letras minúsculas fica assim: {nome.lower()}")
print(f"O seu nome contém {len(''.join(separado))} letras.")
print(f"O seu primeiro nome que é {separado[0]} contém {len(''.join(separado[0]))}")
