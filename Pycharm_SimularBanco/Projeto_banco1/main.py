#canto esquerdo new => file python => nome main

#dois arquivos na mesma pasta ContasdeBancos.py e main.py
#puxar as informacoes das ContasBancos.py
#import ContasBancos
#ContasBancos.ContaCorrente
#ContasBancos.CartaCredito
#NESTE não roda o ARQUIVO AGENCIAversao2.PY, pois tem o arquivo
#este usa arquivo main.py, Agenciaversao2.py e ContasdeBancos.py

from ContasdeBancos import ContaCorrente, CartaoCredito
import time
#main.py
#code atalhos ctrl /
#from Agencia import  AgenciaComum,AgenciaPremium, AgenciaVirtual
from Agenciaversao2 import  AgenciaComum,AgenciaPremium, AgenciaVirtual
#um espaço entre os def dentro da classe e dois no final da class
# programa
def digita_cpf():
    cpf_coleta = input("Qual seu cpf (escrever como: 000.000.000-00")
    print(cpf_coleta)
    return cpf_coleta


print(len("111.222.333-45"))
letras = 14
#cpf_coleta=str(digita_cpf())
cpf_coleta="111.222.333-45"
quantidade_letra = len(cpf_coleta)
print(quantidade_letra)
valido=False
while valido == False:
   quantidade_letra = len(cpf_coleta)
   if quantidade_letra == letras:
      valido = True
      print(valido)
      break
   else:
      print("Digite novamente")
      cpf_coleta = str(digita_cpf())
      valido = False

#conta_Cliente1 = ContaCorrente("José Lira", "111.222.333-45")
conta_Cliente1 = ContaCorrente("José Lira", cpf_coleta,1234, 34073)

print("*-"*20)
print('Saldo da conta aberta no momento R$ {}'.format(conta_Cliente1._saldo))
print('CPF do dono da conta {}'.format(conta_Cliente1._cpf))

#conta_Lira = conta_Cliente1
print(conta_Cliente1.consultar_saldo())
print("*-"*20)


conta_Cliente1.depositar(100)
#conta_Cliente1.saldo = conta_Cliente1.saldo + 100
print('Saldo da conta após aberta (depositaram, no momento: R$ {}'.format(conta_Cliente1._saldo))


#adicionei mais 1000 reais
#conta_Cliente1.saldo = conta_Cliente1.saldo + 1000
conta_Cliente1.depositar(1000)
print("=="*20)
print(conta_Cliente1.consultar_saldo())
print("=="*20)

print("=="*20)
#depositando o dinheiro na conta
print('depositando o dinheiro na conta R$ 10,000.00')
conta_Cliente1.depositar(10000)
conta_Cliente1.consultar_saldo()
time.sleep(3)
#sacando o dinheiro na conta
print('sacando o dinheiro na conta R$ 1,000.00')
conta_Cliente1.sacar_dinheiro(1000)
conta_Cliente1.consultar_saldo()
print("=="*20)

#sacando o dinheiro na conta
print('sacando o dinheiro na conta R$ 100,000.00')
conta_Cliente1.sacar_dinheiro(100000)
conta_Cliente1.consultar_saldo()
print("=="*20)

#depositando o dinheiro na conta
print('depositando o dinheiro na conta R$ 200,000.00')
conta_Cliente1.depositar(200000)
conta_Cliente1.consultar_saldo()
#verificar regras, definir para sacar o que quiser
print()
print("=="*20)
#sacando o dinheiro na conta
print('sacando o dinheiro na conta R$ 500.00')
conta_Cliente1.sacar_dinheiro(500)
conta_Cliente1.consultar_saldo()
print("=="*20)


print()
print("=="*20)
#sacando o dinheiro na conta
print('sacando o dinheiro na conta R$ 210,600.00')
conta_Cliente1.sacar_dinheiro(210600.00)
conta_Cliente1.consultar_saldo()
print("=="*20)

print()

#depositando o dinheiro na conta
print('depositando o dinheiro na conta R$ 280,000.00')
conta_Cliente1.depositar(280000)
conta_Cliente1.consultar_saldo()
#verificar regras, definir para sacar o que quiser
print()
print('Saldo final da conta:')
conta_Cliente1.consultar_saldo()
conta_Cliente1.consultar_limite_chefeespecial()
print("=="*20)

print('#'* 35)
#print(conta_Cliente1.transacoes)
conta_Cliente1.consultar_historicos_transacoes()

Conta_Segundo_cliente = ContaCorrente('Elizabethy', '222.333.444-55',5555,656575)

print('Transferir R$ 1000 da conta principal, de {}, para o segundo cliente: {}'.format(conta_Cliente1._nome_cliente, Conta_Segundo_cliente._nome_cliente))
conta_Cliente1.transferir(1000, Conta_Segundo_cliente)

print('#'* 35)
print('Consultar o saldo de {}'.format(conta_Cliente1._nome_cliente))
conta_Cliente1.consultar_saldo()
print('#'* 35)
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente._nome_cliente))
Conta_Segundo_cliente.consultar_saldo()
print('#'* 35)
print()

print('#'* 35)
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente._nome_cliente))
conta_Cliente1.consultar_historicos_transacoes()
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente._nome_cliente))
Conta_Segundo_cliente.consultar_historicos_transacoes()
print('#'* 35)

help(ContaCorrente)
print('')
#help(str)

cartao_cliente1 = CartaoCredito('Jose Lira', conta_Cliente1)
print('Nome do titular do Cartão de Crédito: {}'.format(cartao_cliente1.titular))
print(cartao_cliente1.conta_corrente)
print('Número da conta corrente:')
print(cartao_cliente1.conta_corrente._num_conta)
print()
print('Cartões de {}'.format(conta_Cliente1._nome_cliente))
print(conta_Cliente1.cartoes)
print('Número do cartão:')
print(conta_Cliente1.cartoes[0].numero)
print('Nome de quem tem o numero do cartão:')
print(conta_Cliente1.cartoes[0].titular)
#print(conta_Cliente1.cartoes[0].conta_corrente)
print('Validade do Cartão de {}'.format(conta_Cliente1._nome_cliente))
print(cartao_cliente1.validade)
print('Código de segurança {} do Cartão de {}, com o cpf {}'.format(cartao_cliente1.cod_seguranca, conta_Cliente1._nome_cliente, conta_Cliente1._cpf))

print("Alterar o nome:")
#get = entrar com os dados
#setar = mudar
#metodos getter e setter
#mas o ideal é o nome do cliente tirar o underline no início
conta_Cliente1._nome_cliente = "AKatarina Dias"
print('Nome do cliente do Cartão: {}'.format(conta_Cliente1._nome_cliente))

#podemos usar sem o _, mas o _ é o indicador para ser restrito
cartao_cliente1.senha = '12'
print('Trocando a senha \n A senha atual é :{}'.format(cartao_cliente1.senha))
print('Trocando a senha \n A senha atual é :{}'.format(cartao_cliente1._senha))

senha_nova_credito = (input("Sua senha nova de 4 digitos"))
cartao_cliente1.senha = str(senha_nova_credito)
print('Trocando a senha \n A senha atual é :{}'.format(cartao_cliente1.senha))
print('-------teste--------------------')
print(senha_nova_credito)
print(senha_nova_credito.isnumeric())
print(str(senha_nova_credito))
print(str(senha_nova_credito).isnumeric())


print("Atributos 'conta_Cliente1'")
#método dos dicionarios com os atributos
print(conta_Cliente1.__dict__)
print()
print("Atributos 'cartao_cliente1'")
print(cartao_cliente1.__dict__)
print("Atributos 'Conta_Segundo_cliente'")
print(Conta_Segundo_cliente.__dict__)


print('-----------------------Agencia----------------------')
print('----------------------------------------------------')
print('Agencia Premium')
agencia_premium_especial = AgenciaPremium(221222222, 15888888888)
#print(agencia_premium_especial)
print(agencia_premium_especial.clientes)
print('Agência Premium e seu número:{}, \ncnpj: {} ,\nTelefone: {}'.format(agencia_premium_especial.numero, agencia_premium_especial.cnpj, agencia_premium_especial.telefone))
print('Caixa da Agencia Premium, R${:,.2f}'.format(agencia_premium_especial.caixa))