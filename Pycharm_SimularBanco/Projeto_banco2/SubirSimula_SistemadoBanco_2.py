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

#help(ContaCorrente)
print('')
#help(str)

#inserir o nome do cliente 1 e da sua conta corrente, para ver o cartao de credito
cartao_cliente1 = CartaoCredito(nome_coleta, conta_Cliente1)
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
#print(conta_Cliente1._cartoes[0].conta_corrente)
print(conta_Cliente1.cartoes[0].titular)
print('Validade do Cartão de {}'.format(conta_Cliente1._nome_cliente))
print(cartao_cliente1.validade)
print('Código de segurança {} do Cartão de {}, com o cpf {}'.format(cartao_cliente1.cod_seguranca, conta_Cliente1._nome_cliente, conta_Cliente1._cpf))

print("Quer alterar o nome da conta?")
resposta_altera = str(input("Sim ou Não"))

resposta_altera = resposta_altera.lower()

if resposta_altera in 'sim':
    #get = entrar com os dados
    #setar = mudar
    #metodos getter e setter
    #mas o ideal é o nome do cliente tirar o underline no início
    #conta_Cliente1._nome_cliente = "AKatarina Dias"
    conta_Cliente1._nome_cliente = str(input("Adicionar seu nome e sobrenome"))
else:
    pass

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
