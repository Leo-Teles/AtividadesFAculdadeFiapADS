

assinatura = ""

while assinatura != "BASIC" "SILVER"  "GOLD" "PLATINUM":
    assinatura = input("Qual sua assitura? ")
    assinatura_upper = assinatura.upper()


    if assinatura.upper() == "BASIC":
        faturamentoAnual = float(input("Digite seu faturamento anual: "))
        bonusAnual = faturamentoAnual * 0.3
        print("Seu faturamento anual é de R${}" .format(bonusAnual))

        break

    elif assinatura_upper == "SILVER":
        faturamentoAnual = float(input("Digite seu faturamento anual: "))
        bonusAnual = faturamentoAnual * 0.2
        print("Seu faturamento anual é de R${}".format(bonusAnual))
        break

    elif assinatura_upper == "GOLD":
        faturamentoAnual = float(input("Digite seu faturamento anual: "))
        bonusAnual = faturamentoAnual * 0.1
        print("Seu faturamento anual é de R${}".format(bonusAnual))
        break

    elif assinatura_upper == "PLATINUM":
        faturamentoAnual = float(input("Digite seu faturamento anual: "))
        bonusAnual = faturamentoAnual * 0.05
        print("Seu faturamento anual é de R${}".format(bonusAnual))
        break

    else:
        print("Digite sua assinatura correta!! ")


print("Até mais!! ")

