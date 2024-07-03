# sistema de banco, classe das contas dos bancos
# lógicas das contas
#class comeca com letra maiúscula e separa com maiúscula (sugestão)

#(base) nome@root:~/Documentos/CRIACAO-HD/NOTA-PYTHON-LIRA/42-Orientacao_a_Objetos_completo/pycharm-community-2024.1.3/bin$ ./pycharm.sh 

#fonte para ativar a minha máquina virtual, no seu terminal
#source /home/nomedapessoa/Documentos/CRIACAO-HD/NOTA-PYTHON-LIRA/42-Orientacao_a_Objetos_completo/Projeto_mod42/pythonProject1/venv/bin/activate
#depois eu instalo nesta máquina virtual
#(venv) (base) nomedapessoa@computador:~/Documentos/CRIACAO-HD/NOTA-PYTHON-LIRA/42-Orientacao_a_Objetos_completo/pycharm-community-2024.1.3/bin$ pip install pytz
#pip install pytz

from datetime import datetime
#ajuste de fuzo horário pytz
import pytz
#pip install pytz
import time

#pode ser assim: class ContaCorrente:

class ContaCorrente():
    """

    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Attributos:

    Nome (str): Nome do Cliente
    cpf (str): CPF do cliente
    Agencia (int): Agencia do responsável pela conta do cliente
    num_conta (int): Número da Conta Corrente do Cliente
    Saida(float): Saldo disponível da conta do cliente
    limite(float): Limite de Cheque especial daquele cliente
    transacoes: Histórico de Transações do Cliente
    #PEP 257 DOCSTRING -> padrão de explicação dos códigos


    """

    #procurar a data e hora atual (método estático), auxiliar e não público (_comeco)
    @staticmethod #sinalizacao
    def _data_hora():
        # fuso horario de brasilia
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        print('---horario---')
        print(horario_BR)
        #return horario_BR
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    # parâmetro da conta
    # criada com o saldo =0
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome_cliente = nome
        self.cpf = cpf
        self.saldo = 0
        #limite colocando como dado zerado
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        # adcionar a funcionalidade, consultar o histórico.
        self.transacoes =[]

    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta do cliente
        não há parâmetros necessários

        """
        print('Seu saldo atual é de R$ {:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        #pass
        #consultar
        self.consultar_saldo()
        # valor que adcionou, 'Saldo:{}', data e hora
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        print('-----entrando no sistema ----')
        print(valor, self.saldo, ContaCorrente._data_hora())
    # criar o método para sacar, se tem saldo
    # conta do limite
    #  o _ na funcao é para identificar como método privado.

    def _limite_conta(self):
        #dados para verificar o limite
        # não funciona => self.limite = self.limite  - 1000
        #limite de 1000 reais
        self.limite = - 1000
        return self.limite

    def sacar_dinheiro(self,valor):
        #verificando o limite
        if self.saldo - valor < self._limite_conta():
        #if self.saldo - valor < 0:
           print('Você não tem saldo suficiente para sacar esse valor')
           print()
           #chamar função dentro da função tem que usar self.
           self.consultar_saldo()

        #caso contrario, fazemos o saque
        else:
           self.saldo -= valor
           self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        #pass



    def consultar_limite_chefeespecial(self):
        print("Seu limite de Cheque Especial é de R$ {:,.2f}".format(self._limite_conta()))


    def consultar_historicos_transacoes(self):
        print('Histórico de transações:')
        print('-' * 62)
        print('|{:^3}  |  {:^13}|  {:^13}|{:^23}|'.format("n","Valor","Saldo","Data e hora"))
        #print('| Valor | Saldo | Data e hora')
        print('-'*62)
        for j, transacao in enumerate(self.transacoes):
            print('|{:^3}°)|R${:^13,.2f}|R${:^13,.2f}|{:^23}|'.format(j+1,transacao[0],transacao[1],transacao[2]))
            #print(transacao)
        print('-' * 62)



    #Duas contas conversarem entre si
    #conta, valor, conta do destino (objeto->outra instancia ou conta)
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        #conta_destino, tem o mesmo parametro da ContaCorrente
        conta_destino.saldo +=valor
        #classe com um todo ContaCorrente._data_hora()
        #self conta onde estou mexendo na conta
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

#um espaço entre os def dentro da classe e dois no final da class
# programa
def digita_cpf():
    cpf_coleta = input("Qual seu cpf (escrever como: 000.000.000-00")
    print(cpf_coleta)
    return cpf_coleta

def inserir_NOME():
    name_enter = input("Qual o nome da conta")
    return name_enter

#print(len("111.222.333-45"))
letras = 14
cpf_coleta=str(digita_cpf())
#cpf_coleta="111.222.333-45"
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


nome_coleta = str(inserir_NOME())
#conta_Cliente1 = ContaCorrente("José Lira", "111.222.333-45")
#conta_Cliente1 = ContaCorrente("José Lira", cpf_coleta,1234, 34073)
conta_Cliente1 = ContaCorrente(nome_coleta, cpf_coleta,1234, 34073)

print("*-"*20)
print('Saldo da conta aberta no momento R$ {}'.format(conta_Cliente1.saldo))
print('CPF do dono da conta {}'.format(conta_Cliente1.cpf))

#conta_Lira = conta_Cliente1
print(conta_Cliente1.consultar_saldo())
print("*-"*20)


conta_Cliente1.depositar(100)
#conta_Cliente1.saldo = conta_Cliente1.saldo + 100
print('Saldo da conta após aberta (depositaram, no momento: R$ {}'.format(conta_Cliente1.saldo))


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

print('Transferir R$ 1000 da conta principal, de {}, para o segundo cliente: {}'.format( conta_Cliente1.nome_cliente, Conta_Segundo_cliente.nome_cliente))
conta_Cliente1.transferir(1000, Conta_Segundo_cliente)

print('#'* 35)
print('Consultar o saldo de {}'.format(conta_Cliente1.nome_cliente))
conta_Cliente1.consultar_saldo()
print('#'* 35)
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente.nome_cliente))
Conta_Segundo_cliente.consultar_saldo()
print('#'* 35)
print()

print('#'* 35)
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente.nome_cliente))
conta_Cliente1.consultar_historicos_transacoes()
print('Consultar o saldo de {}'.format(Conta_Segundo_cliente.nome_cliente))
Conta_Segundo_cliente.consultar_historicos_transacoes()
print('#'* 35)

help(ContaCorrente)
print('')
help(str)
