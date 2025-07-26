import textwrap
menu = """

    [d] depósito
    [l] levantamento
    [c] consulta
    [s] sair

"""

saldo = 0

limite_de_levantamento = 500

consulta = ""

numero_de_levantamento = 0

limite_numero_de_levantamentos = 3

while True:
    
    opcao = input(menu)

    if opcao == "d" :
        valor = float(input("Informe o montante a ser depositado"))
        
        if valor > 0 :

            saldo += valor

            consulta += f"Depósito : R$ {valor:.2f}\n"

        else:
            print("Valor inválido")  

    elif opcao == "l" : 
            valor = float(input("Informe o montante a ser retirado"))

            valor_indisponivel = valor > saldo

            antigiu_limite = valor > limite_de_levantamento

            antigiu_limite_saques = numero_de_levantamento >= limite_numero_de_levantamentos

            if valor_indisponivel :
                 print("Saldo insuficiente")

            elif  antigiu_limite :
                 print("Limite de retirada antigido")

            elif antigiu_limite_saques :
                 print("Limite de antigido")
            
            elif valor > 0 :
                 saldo -= valor

                 consulta += f"Levantamento : R$ {valor:.2f}\n"

                 numero_de_levantamento += 1
            else:
                 print("Saldo não é suficiente")

      
    elif opcao == "c" :
         print("\n======== Extrato ========")

         print("não foram realizados movimentos" if not consulta else consulta)

         print(f"\nSaldo:R${saldo:.2f}")

         print("=========================================")
    
    elif opcao == "q" :
         
         break
    else:
         print("Operação inválida, por favor selecione novamente a operação desejada")
         
