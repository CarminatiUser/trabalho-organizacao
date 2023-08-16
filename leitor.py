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

# Dicionário de cases
cases = {
    "0110111": case_u,
    "0010111": case_u,
    "1101111": case_j,
    "1100111": case_i,
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

desempenho_org1 = []
desempenho_org2 = []

# Loop para solicitar valores duas vezes
for _ in range(2):
    clock = int(input("Informe o clock: "))
    print("Ciclos por Instrução: ")
    ciclos_u = int(input("Tipo U: "))
    ciclos_j = int(input("Tipo J: "))
    ciclos_i = int(input("Tipo I: "))
    ciclos_b = int(input("Tipo B: "))
    ciclos_s = int(input("Tipo S: "))
    ciclos_r = int(input("Tipo R: "))
    ciclos_totais = 0
    
    # Abre o arquivo .txt, e separa ele em linhas
    with open('input.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Salva os ultimos 7 caracteres de cada linha na variavel binarios
    binarios = [linha[-8:].strip() for linha in linhas]
    
    # Mostra todas as instrucoes
    for contador, binario in enumerate(binarios, start=1):
        print(f"Instrucao {contador}: {binario}")
    
    # Mostra o resultado de cada binario depois de passar pelo switch_case
    for contador, binario in enumerate(binarios, start=1):
        resultado = switch_case(binario)
        if resultado != "Opção inválida.":
            ciclos_totais += int(resultado)
        print(f"CPI {contador}: {resultado}")
    
    # Apresenta os resultados totais
    print(f"Ciclos totais: {ciclos_totais}")
    print(f"Ciclos totais X Clock: {ciclos_totais * clock}")
    print()
    
    if _ == 0:
        desempenho_org1.append(ciclos_totais * clock)
    else:
        desempenho_org2.append(ciclos_totais * clock)

# Comparação de desempenho e cálculo da diferença
if desempenho_org1[0] < desempenho_org2[0]:
    print("A Organização 1 teve um melhor desempenho.")
    diferenca = desempenho_org2[0] - desempenho_org1[0]
    print(f"A diferença de desempenho foi de {diferenca} ciclos X clock.")
    porcentagem = (desempenho_org1[0]/desempenho_org2[0]) * 100
    print(f"A porcentagem de diferença de desempenho foi de {porcentagem:.2f}%")

elif desempenho_org2[0] < desempenho_org1[0]:
    print("A Organização 2 teve um melhor desempenho.")
    diferenca = desempenho_org1[0] - desempenho_org2[0]
    print(f"A diferença de desempenho foi de {diferenca} ciclos X clock.")
    porcentagem = (desempenho_org2[0]/desempenho_org1[0]) * 100
    print(f"A porcentagem de diferença de desempenho foi de {porcentagem:.2f}%")

else:
    print("As duas organizações tiveram o mesmo desempenho.")
