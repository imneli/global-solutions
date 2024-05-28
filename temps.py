#Turma 1ESPJ

# RM 557789 - Thomaz Morais Neves
# RM 555499 - Matheus Rivera Montovaneli
# RM 555768 - Guilherme Linard


def calcular_aumento_temperatura(temperaturas_atuais, aumento_anual, anos):
    """
    Esta função recebe uma lista de temperaturas atuais do mar, um aumento anual
    na temperatura do mar e a quantidade de anos desejada para a projeção.
    Retorna uma lista com as temperaturas projetadas para os próximos anos.
    """
    temperaturas_futuras = []
    for temp in temperaturas_atuais:
        temp_futuras = []
        for _ in range(anos):  
            temp += aumento_anual
            temp_futuras.append(temp)
        temperaturas_futuras.append(temp_futuras)
    return temperaturas_futuras

def exibir_temperaturas(temperaturas_futuras, regioes, anos):
    """
    Esta função recebe uma lista de listas com as temperaturas futuras, os nomes das regiões
    e a quantidade de anos. Exibe as temperaturas futuras para cada região ao longo dos anos.
    """
    for i in range(len(temperaturas_futuras)):
        print(f"Temperaturas futuras para a {regioes[i]} ao longo dos próximos {anos} anos:")
        ano = 1
        for temp in temperaturas_futuras[i]:
            print(f"Ano {ano}: {temp:.2f}°C")
            ano += 1
        print()

temperaturas_atuais = [15.0, 20.5, 22.3, 18.7, 20.7] # Temperaturas atuais do mar em diferentes regiões (em graus Celsius)

regioes = ["Região Norte", "Região Sul", "Região Leste", "Região Oeste", "Região Central"] # Nomes das regiões correspondentes as temperaturas atuais

# Loop para solicitar ao user a quantidade de anos desejada
while True:
    anos = int(input("Quantos anos deseja projetar as temperaturas futuras (de 1 a 50)?\n->"))
    if 1 <= anos <= 50:
        break
    else:
        print("Por favor, insira um número válido de anos (de 1 a 50).")

# Aumento anual previsto na temperatura do mar (em graus celsius)
aumento_anual = 0.2

temperaturas_futuras = calcular_aumento_temperatura(temperaturas_atuais, aumento_anual, anos) # Calculando as temperaturas futuras

exibir_temperaturas(temperaturas_futuras, regioes, anos) # Exibindo as temperaturas futuras
