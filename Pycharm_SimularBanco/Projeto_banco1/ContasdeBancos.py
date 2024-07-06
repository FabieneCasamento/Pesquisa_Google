# sistema de banco, classe das contas dos bancos
# lógicas das contas
#class comeca com letra maiúscula e separa com maiúscula (sugestão)

#fonte para ativar a minha máquina virtual, no seu terminal
#source /home/casamentos/Documentos/CRIACAO-HD/NOTA-PYTHON-LIRA/42-Orientacao_a_Objetos_completo/Projeto_mod42/pythonProject1/venv/bin/activate
#depois eu instalo nesta máquina virtual
#(venv) (base) casamentos@dv6500:~/Documentos/CRIACAO-HD/NOTA-PYTHON-LIRA/42-Orientacao_a_Objetos_completo/pycharm-community-2024.1.3/bin$ pip install pytz
#pip install pytz

#no programa ContasdeBancos.py fica apenas as classes
#arquivo main.py que ficam os arquivos

from datetime import datetime
#ajuste de fuzo horário pytz
import pytz
#pip install pytz
import time
#criar numeros aleatórios
from random import randint


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
        # o _ diz que é um método para não ser público, não deve ser alterado
        # o atributo também tem esse tipo de análise, igual o cpf
        # se for __agencia, só terá acesso dentro da classe, por fora não cons
        #só quem está interno, da programação tem acesso ao valor, quem está de fora não tem acesso ao __
        #renomear usando o refactor, botao direito => rename => refactor +> do refactor
        self._nome_cliente = nome
        self._cpf = cpf
        self._saldo = 0
        #limite colocando como dado zerado
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        # adcionar a funcionalidade, consultar o histórico.
        self._transacoes =[]
        # olhar a conta corrente, e ver os cartoes conta corrente
        self.cartoes = []


    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta do cliente
        não há parâmetros necessários

        """
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        #pass
        #consultar
        self.consultar_saldo()
        # valor que adcionou, 'Saldo:{}', data e hora
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        print('-----entrando no sistema ----')
        print(valor, self._saldo, ContaCorrente._data_hora())
    # criar o método para sacar, se tem saldo
    # conta do limite
    #  o _ na funcao é para identificar como método privado.

    def _limite_conta(self):
        #dados para verificar o limite
        # não funciona => self.limite = self.limite  - 1000
        #limite de 1000 reais
        self._limite = - 1000
        return self._limite

    def sacar_dinheiro(self,valor):
        #verificando o limite
        if self._saldo - valor < self._limite_conta():
        #if self.saldo - valor < 0:
           print('Você não tem saldo suficiente para sacar esse valor')
           print()
           #chamar função dentro da função tem que usar self.
           self.consultar_saldo()

        #caso contrario, fazemos o saque
        else:
           self._saldo -= valor
           self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        #pass



    def consultar_limite_chefeespecial(self):
        print("Seu limite de Cheque Especial é de R$ {:,.2f}".format(self._limite_conta()))


    def consultar_historicos_transacoes(self):
        print('Histórico de transações:')
        print('-' * 62)
        print('|{:^3}  |  {:^13}|  {:^13}|{:^23}|'.format("n","Valor","Saldo","Data e hora"))
        #print('| Valor | Saldo | Data e hora')
        print('-'*62)
        for j, transacao in enumerate(self._transacoes):
            print('|{:^3}°)|R${:^13,.2f}|R${:^13,.2f}|{:^23}|'.format(j+1,transacao[0],transacao[1],transacao[2]))
            #print(transacao)
        print('-' * 62)



    #Duas contas conversarem entre si
    #conta, valor, conta do destino (objeto->outra instancia ou conta)
    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        #conta_destino, tem o mesmo parametro da ContaCorrente
        conta_destino._saldo +=valor
        #classe com um todo ContaCorrente._data_hora()
        #self conta onde estou mexendo na conta
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))



#criar a classe Cartão de Crédito

class CartaoCredito:

     @staticmethod  # sinalizacao da segunda classe
     def _data_hora():
        # fuso horario de brasilia
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        print('---horario---')
        print(horario_BR)
        return horario_BR

     #conta_corrente, quem qual está associado
     def __init__(self, titular, conta_corrente):
         #self.numero = None
         #self.numero = 123
         # gerar de 1 a 16 numeros, que cada um vai de 0 a 9
         self.numero = randint(1000000000000000, 9999999999999999)
         self.titular = titular
         #nome=titular
         # self.validade = CartaoCredito._data_hora() colocar mais 4 anos
         self.validade = '{}/{}'.format(CartaoCredito._data_hora().month,CartaoCredito._data_hora().year +4 )
         # gerar de 1 a 3 numeros, que cada um vai de 0 a 9 no codigo de seguranca
         # mas assim nao comeca com zero, ter quer ser com texto randint(100, 999)
         self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
         #self.cod_seguranca = None
         #limite de 1000 reais
         self.limite = 1000
         self.conta_corrente = conta_corrente
         #adicionar o cartao de credito dentro da conta corrente
         #self = instancia do cartao de credito
         # quero restringir a senha, fazendo um método
         self._senha = '1234'
         conta_corrente.cartoes.append(self)
         #conta_corrente._cartoes.append(self.numero) #entra apenas o numero

     #método get
     # senha é um atributo
     #def tem que ter o mesmo nome do self._senha => no caso senha(self): para funcionar
     #pois é o nome do atributo
     #nao funcionaria se fosse def ourosenha(self):
     @property
     def senha(self):
         #logica
         #pass
         return self._senha


     #restricao na hora de modificar a senha
     @senha.setter
     def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
           self._senha = valor
        else:
           print("Nova Senha inválida")
