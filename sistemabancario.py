import textwrap

def menu():

     menu = """\n
     ____________________ MENU ____________________

     [d]\tdepósito
     [l]\tlevantamento
     [c]\tconsulta
     [nc]\tNova conta
     [lc]\tListar conta
     [nu]\tNovo usuario
     [s]\tsair

           =>"""
     return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):

     if valor > 0 :
          saldo += valor
          extrato += f"Depósito : \tR$ {valor:.2f}\n"
          print("Depósito efectuado com sucesso")
     else:
           print("\n@@@ operação falhou")

     return saldo,extrato
     
def sacar(*,saldo,valor,extrato,limite, numero_saque,Limites_saques):
      
      excedeu_saldo =  valor > saldo
      excedeu_limite = valor > limite
      excedeu_saques = numero_saque > Limites_saques
      
      if excedeu_saldo :
             print("\n@@@ operação falhou, saldo insuficiente")

      elif excedeu_limite:
             print("\n@@@ operação falhou, limite do valor de retirada atingido")

      elif excedeu_saques :
             print("\n@@@ operação falhou, limite de saque atingido")
            
      elif valor > 0 :
            saldo -= valor
            extrato += f"Saque:\t\tR${valor:.2f}\n"
            numero_saque += 1
            print("\n@@@ Saque realizado com sucesso")
            
      else:
          print("\n@@@ operação falhou,valor inválido")
      
      return saldo, extrato

def exibir_extrato(saldo, /,*, extrato):
      print("\n======== Extrato ========")

      print("não foram realizados movimentos" if not extrato else extrato)

      print(f"\nSaldo:R${saldo:.2f}")

      print("=========================================")    

def criar_usuario(usuarios):
      cpf = input("Informe o cpf(somente número)")
      usuario = filtrar_usuario(cpf,usuarios)

      if usuario :
          print("\n@@@ Já existe usuario com esse CPF")
          return
      
      nome = input("Informe o seu nome completo")
      data_nascimento = input("Informe o sua data de nascimento")
      endereco =input("Informe o seu endereco")

      usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco,"cpf":cpf})
      print("Conta registrada com sucesso")

def filtrar_usuario(cpf,usuarios):
      usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
      return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(Agencia,numero_conta,usuarios):
      cpf =  cpf = input("Informe o cpf")
      usuario = filtrar_usuario(cpf,usuarios)

      if usuario :
          print("\n@@@ Conta criada com sucesso")
          return {"Agencia" : Agencia,"numero_conta": numero_conta, "usuario": usuario}
      
      print("\n@@@Falha na criação da conta")

def listar_contas(contas):
     for conta in contas:
           linha = f"""\
               Agencia: \t{conta['agencia']}
               C/C :\t\t{conta['numero_conta']}
               Titular: \t{conta['usuario']['nome']}
          """
           print("=" * 100)
           print(textwrap.dedent(linha))
           
def main():
     Limite_saques = 3
     Agencia = "0001"

     saldo = 0
     limite= 500
     extrato = ""
     numero_saque = 0
     usuarios = []
     contas = []

     while True:
     
          opcao = menu()


     if opcao == "d" :
          valor = float(input("Informe o montante a ser depositado"))

          saldo, extrato = depositar(saldo,valor,extrato)

     elif opcao == "l" : 
               valor = float(input("Informe o montante a ser retirado:"))

               saldo, extrato = sacar(
                   
                     saldo = saldo,
                     valor = valor,
                     extrato = extrato,
                     limite= limite,
                     numero_saque = numero_saque,
                     lomite_saque = Limite_saques
          
                   )
               
     elif opcao == "c" :
          print("\n======== Extrato ========")
          exibir_extrato(saldo,extrato=extrato)
     
     elif opcao == "nu" :

          criar_usuarios(usuarios)
          
     elif opcao == "nc" :

          numero_conta =len(contas) + 1
          conta = criar_conta(Angencia, numero_conta, usuarios)

          if conta :
                contas.append(conta)
     
     elif opcao == "lc" :
           
           listar_contas(contas)
          
     elif opcao == "s" :
        breakpoint
     else:
          print("Operação inválida, por favor selecione novamente a operação desejada")
     
main()
