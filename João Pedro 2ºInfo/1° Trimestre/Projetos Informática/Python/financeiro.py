print("Qual tipo de investimento voce gostaria de fazer?")
investimentos = [
    "1-Prefixado",
    "2-Posfixado",
    "3-TesouroSelic",
    "4-CDB",
    "5-LCI",
    "6-LCA",
]
opcoes = {
    1: "Prefixado",
    2: "Posfixado",
    3: "TesouroSelic",
    4: "CDB",
    5: "LCI",
    6: "LCA",
}

print()


for investimento in investimentos:
    print(investimento)
print()

while True:    
    try:
        TipoDeInvestimento = int(input("Digite o numero da opcao:"))
        if TipoDeInvestimento in opcoes:
            print()
            print("Voce escolheu", f'{opcoes[TipoDeInvestimento]}')
            print()
            break
        else:
            print()
            print("Digite uma opção válida")
            print()
    except:
            print()
            print("Digite uma opção válida")
            print()


while True:
    print("Quanto voce quer investir?")
    try:
        ValorInicial = float(input("Digite em decimal (Exemplo: 100.00):"))
        print()
        break
    except: 
        print()
        print("digite um número por favor")
   
print()

while True:
    print("Por quantos Meses quer investir?")
    try:
        Tempo = float(input("Meses:"))
        print()
        break
    except:
        print()
        print("Dígite um Número")
        print()

while True:
    if TipoDeInvestimento == 1:
        ValorBruto = (ValorInicial * (1 + 0.11)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro * (1 - 22.5 / 100)
        print("Seu lucro será de", {LucroIR})
        break
    elif TipoDeInvestimento == 2:
        ValorBruto = (ValorInicial * (1 + 0.010979)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro * (1 - 22.5 / 100)
        print("Seu lucro será de", {LucroIR})
        break
    elif TipoDeInvestimento == 3:
        ValorBruto = (ValorInicial * (1 + 0.115)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro * (1 - 22.5 / 100)
        print("Seu lucro será de", {LucroIR})
        break
    elif TipoDeInvestimento == 4:
        ValorBruto = (ValorInicial * (1 + 0.010979)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro * (1 - 22.5 / 100)
        print("Seu lucro será de", {LucroIR})
        break
    elif TipoDeInvestimento == 5:
        ValorBruto = (ValorInicial * (1 + 0.010979)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro
        print("Seu lucro será de", {LucroIR})
        break
    elif TipoDeInvestimento == 6:
        ValorBruto = (ValorInicial * (1 + 0.010979)**Tempo)
        Lucro = ValorBruto - ValorInicial
        LucroIR = Lucro
        print("Seu lucro será de", {LucroIR})
        break