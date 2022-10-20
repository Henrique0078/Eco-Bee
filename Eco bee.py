
while True:
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------Programa desenvolvido por 'ECO BEE'-------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")

    print("Quando se falar em hectares no programa, estaremos nos referindo a área de atuação das abelhas.")
    ar_p_ec_ant = float(input("Média de árvores por hectare no momento de ingresso da empresa no local:  "))
    ar_p_ec_atual = float(input("Média de árvores por hectare atual:  "))
    n_ec = float(input("Numero de hectares:  "))
    b3 = float(input("Preço atual do crédito de carbono:  "))
    print("Entre com 'A' para selecionar o periodo atual, deste jeito receberá o valor de créditos de carbono do ano atual ou")
    print("entre com 'B' para selecionar todo o perioso, assim vai ter o total de creditos conseguidos em todos os anos no local.")
    v_periodo = input("Entre com o periodo desejado:  ")



    if (v_periodo == "A") or (v_periodo == "a"):

        mediaatual = (ar_p_ec_atual * n_ec)
        mediaanterior = (ar_p_ec_ant * n_ec)
        total = ((mediaatual - mediaanterior) / 7 * 0.80 / 20)
        totalb3 = (total * b3) #b3 pois e o valor do credito de carbono atualmente

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------Saida de dados------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------------------------")

        print(f"A empresa fez um total de {total:.5f} créditos de carbono\nque por sua vez, valem atualmente R${totalb3:.2f} na B3(Bolsa de Valores)")

    elif (v_periodo == "B") or (v_periodo == "b"):
        ano_ingreco = int(input("Ano de ingresso no local atual:  "))
        ano_atual = int(input("Ano atual:  "))
        anos = (ano_atual - ano_ingreco)
        mediaatual = (ar_p_ec_atual * n_ec)
        mediaanterior = (ar_p_ec_ant * n_ec)
        total = ((mediaatual - mediaanterior) / 7 * 0.80 / 20) * anos
        totalb3 = (total * b3)

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------Saida de dados------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------------------------")

        print(f"A empresa fez no total de {anos} anos de estadia no local\num total de {total:.5f} créditos de carbono,\nque por sua vez, valem atualmente R${totalb3:.2f} na B3(Bolsa de Valores)")

    else:

        print("-------------------------------------------------------------------------------------------------------------------------")
        print("-----------------------------------------------------Saida de dados------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------------------------")

        print(f"Na variavel periodo voce entrou com {v_periodo}, que é invalido, favor entrar com: A ou B.")

    print("-------------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------Programa desenvolvido por 'ECO BEE'-------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------")

    print("Caso deseje sair digite 'sair', se não simplismente pressione ENTER.")
    sair = input("Deseja refazer o processo ou sair:  ").upper()

    if (sair == "SAIR"):
        break

print("Obrigado por escolher 'ECO BEE'")