# Global Solutions - Blue Future 🌊

## Computational Thinking With Python ⚡

<h2> 

<li> RM 557789 - Thomaz Morais Neves
<li> RM 555499 - Matheus Rivera Montovaneli
<li> RM 555768 - Guilherme Linard

</h2> 

## `Código`

`Calcular temperatura`

```PY
def calcular_aumento_temperatura(temperaturas_atuais, aumento_anual, anos):
    temperaturas_futuras = []
    for temp in temperaturas_atuais:
        temp_futuras = []
        for _ in range(anos):  
            temp += aumento_anual
            temp_futuras.append(temp)
        temperaturas_futuras.append(temp_futuras)
    return temperaturas_futuras

```

Esta função recebe uma lista de temperaturas atuais do mar, um aumento anual
na temperatura do mar e a quantidade de anos desejada para a projeção.
Retorna uma lista com as temperaturas projetadas para os próximos anos podendo escolher uma previsão entre 1 a 50 anos.

`Exibir temperaturas`

```PY
def exibir_temperaturas(temperaturas_futuras, regioes, anos):
    for i in range(len(temperaturas_futuras)):
        print(f"Temperaturas futuras para a {regioes[i]} ao longo dos próximos {anos} anos:")
        ano = 1
        for temp in temperaturas_futuras[i]:
            print(f"Ano {ano}: {temp:.2f}°C")
            ano += 1
        print()
```
Esta função recebe uma lista de listas com as temperaturas futuras, os nomes das regiões
e a quantidade de anos. Exibe as temperaturas futuras para cada região ao longo dos anos.

`Listas (Regiões e temperaturas iniciais)`

```PY
temperaturas_atuais = [15.0, 20.5, 22.3, 18.7, 20.7] 

regioes = ["Região Norte", "Região Sul", "Região Leste", "Região Oeste", "Região Central"]
```

É passada uma Lista de Regiões com suas Temperaturas inicias, correspondentes ao indice [ i ], por exemplo 15.0 == Região Norte

`Loop para pedir Input ao usuário`

```PY
while True:
    anos = int(input("Quantos anos deseja projetar as temperaturas futuras (de 1 a 50)?\n->"))
    if 1 <= anos <= 50:
        break
    else:
        print("Por favor, insira um número válido de anos (de 1 a 50).")
```

Looping que solicita a quantidade de anos que o usuário quer prever. Caso seja acima ou abaixo dos anos permitidos ele solicita uma quantidade de anos novamente.

`Aumento Anual estabelecido de 0.2 em Celsius.`

```PY
aumento_anual = 0.2
```

`Calcular e printar Temperaturas do Oceano`

```PY 
temperaturas_futuras = calcular_aumento_temperatura(temperaturas_atuais, aumento_anual, anos) 

exibir_temperaturas(temperaturas_futuras, regioes, anos) 
```

O "temperaturas_futuras" é usado para calcular as temperaturas futuras

E o "exibir_temperaturas" exibe o resultado dos parâmetros passados (temperaturas_futuras, regioes, anos)
