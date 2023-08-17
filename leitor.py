# Cases
def case_u():
    return ciclos_u

def case_j():
    return ciclos_j

def case_i():
    return ciclos_i

def case_b():
    return ciclos_b

def case_s():
    return ciclos_s

def case_r():
    return ciclos_r

def case_i2():
    return ciclos_i2

# Dicionário de cases
cases = {
    "0110111": case_u,
    "0010111": case_u,
    "1101111": case_j,
    "1100111": case_i2,
    "1100011": case_b,
    "0000011": case_i,
    "0100011": case_s,
    "0010011": case_i,
    "0110011": case_r,
    "0001111": case_i,
    "1110011": case_i
}

# Função switch_case
def switch_case(binario):
    func = cases.get(binario, lambda: "Opção inválida.")
    return func()

desempenho_org1 = 0
desempenho_org2 = 0

# Loop para solicitar valores duas vezes
for _ in range(2):
    clock = float(input("Informe o clock: "))
    ciclos_u = float(input("Tipo U: "))
    ciclos_j = float(input("Tipo J: "))
    ciclos_i = float(input("Tipo I: "))
    ciclos_i2 = float(input("Tipo I2: "))
    ciclos_b = float(input("Tipo B: "))
    ciclos_s = float(input("Tipo S: "))
    ciclos_r = float(input("Tipo R: "))
    ciclos_totais = 0
    cont = 0
    
    # Abre o arquivo .txt, e separa ele em linhas
    with open('input.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    # Salva os ultimos 7 caracteres de cada linha na variavel binarios
    binarios = [linha[-8:].strip() for linha in linhas]
    
    print()

    # Mostra todas as instrucoes
    for contador, binario in enumerate(binarios, start=1):
        print(f"Instrucao {contador}: {binario}")
        cont += 1
    
    print()

    # Mostra o resultado de cada binario depois de passar pelo switch_case
    for contador, binario in enumerate(binarios, start=1):
        resultado = switch_case(binario)
        if resultado != "Opção inválida.":
            ciclos_totais += float(resultado)
        print(f"CPI {contador}: {resultado}")
    
    # Apresenta os resultados totais
    print("__________________________________________________________")
    print()
    print(f"Ciclos totais: {ciclos_totais}")
    print(f"CPI média {ciclos_totais / cont: .2f}")
    print(f"Tempo de execução da CPU: {ciclos_totais * clock: .2f}")
    print("__________________________________________________________")
    print()
    
    if _ == 0:
        desempenho_org1 = ciclos_totais * clock
    else:
        desempenho_org2 = ciclos_totais * clock

# Comparação de desempenho e cálculo da diferença
if desempenho_org1 < desempenho_org2:
    print("A Organização 1 teve um melhor desempenho.")
    print()

    diferenca = desempenho_org2 - desempenho_org1
    print(f"A diferença de desempenho foi de {diferenca: .2f} nanosegundos.")

    porcentagem = (diferenca)/desempenho_org1 * 100
    print(f"A porcentagem de diferença de desempenho foi de {porcentagem:.2f}%")

    vezes = (desempenho_org2 / desempenho_org1)
    print(f"A diferença de desempenho foi de {vezes:.2f} vezes")


elif desempenho_org2 < desempenho_org1:
    print("A Organização 2 teve um melhor desempenho.")
    print()

    diferenca = desempenho_org1 - desempenho_org2
    print(f"A diferença de desempenho foi de {diferenca: .2f} nanosegundos.")

    porcentagem = (diferenca)/desempenho_org2 * 100
    print(f"A porcentagem de diferença de desempenho foi de {porcentagem:.2f}%")

    vezes = (desempenho_org1 / desempenho_org2)
    print(f"A diferença de desempenho foi de {vezes:.2f} vezes")

else:
    print("As duas organizações tiveram o mesmo desempenho.")

print("__________________________________________________________")
print()
