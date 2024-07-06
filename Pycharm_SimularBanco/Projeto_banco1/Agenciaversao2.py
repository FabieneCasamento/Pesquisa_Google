#classes e subclasse Agencia
from random import randint


class Agencia:
    # telefone, cnpj, numero da conta
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.cnpj = cnpj
        # agencia pode fazer imprestimos para os clientes
        self.emprestimos = []


    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O Valor de Caixa está ok. Caixa Atual {}'.format(self.caixa))


    def emprestar_dinheiro(self, valor, cpf, juros):
         if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
         else:
            print('Empréstimo não é possível. Dinheiro não disponível em Caixa.')


    #como as classes se interagem com as outras classes
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


#classes filhas da Agencia
#AgenciaVirtual
#AgenciaComum
#AgenciaPremium

#editar os metodos como heranca, comum e virtual nao tem tanto criterio
#ja na premium tem mais criterio

#classes filhas da Agencia
class AgenciaVirtual(Agencia):
    # tem que personalisar o init, se nao pega o init da classe da Agencia princial
    def __init__(self, site, telefone,cnpj):
        self.site = site
        #usar o init tambem da sua super classe, no caso Agencia
        #super().__init__(telefone, cnpj, numero)
        super().__init__(telefone, cnpj, 1000)
        #um milhão de reais
        self.caixa = 1000000
        #virtual caixa_paypal, para transferência
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        #tirar o valor do caixa
        self.caixa -= valor
        # e colocar dentro do paypal
        self.caixa_paypal += valor


    def sacar_paypal(self, valor):
        #tirar o valor do paypal
        self.caixa_paypal -= valor
        # e colocar dentro do caixa geral
        self.caixa += valor


class AgenciaComum(Agencia):
    # comum
    def __init__(self, telefone, cnpj):
        # numero aleatório
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 1000000
        #pass


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        # numero aleatório
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 20000000
        #pass

        # editar os metodos como heranca, comum e virtual nao tem tanto criterio
        # ja na premium tem mais criterio

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            print('Adicionar o cliente')
            # nao ficar copiando toda hora, apenas chama a funcao da classe principal (Agencia)
            super().adicionar_cliente(nome, cpf, patrimonio)
         #   self.clientes.append((nome, cpf, patrimonio))
        else:
            print('O Cliente não tem o patrimônio mínimo necessário para entrar na Agência Premium')


#teste 1
# só roda dentro deste arquivo, serve para testar
if __name__ == '__main__':

    agencia1 = Agencia(222233333, 3225325325, 4568)
    print('Agência e seu número:{}, \ncnpj{} ,\nTelefone:{}'.format(agencia1.numero, agencia1.cnpj, agencia1.telefone))
    agencia1.verificar_caixa()
    #print('Agência e seu número:{}'.format(agencia1.numero))

    #teste2 colocando o dinheiro no caixa
    agencia1.caixa = 1000000
    print('Dinheiro colocado no caixa da agência {}'.format(agencia1.caixa))
    agencia1.verificar_caixa()


    print('Empréstimo de {}, para o portador do CPF:{}\nCom {}% de juros'.format(1500, 1412414312313, 0.02*100))
    agencia1.emprestar_dinheiro(1500, 1412414312313, 0.02)
    print('Verificar se foi feito o empréstimo:')
    print(agencia1.emprestimos)
    print('Emprestimo ok de R${:,.2f}'.format(agencia1.emprestimos[0][0]))

    agencia1.adicionar_cliente('Paulo NewGame', 121414345523, 10000)
    print(agencia1.clientes)

    print('Nome do cliente novo {}\ncom o CPF:{},\nE seu empréstimo de R${:,.2f}'.format(agencia1.clientes[0][0],agencia1.clientes[0][1],agencia1.clientes[0][2] ))
    print()

    print('Agência Virtual')
    #telefone, cnpj e agencia
    #agencia_virtual = AgenciaVirtual(2222213133,1520000000,1000)
    #print('Agência Virtual e seu número:{}, \ncnpj: {} ,\nTelefone: {}'.format(agencia_virtual.numero, agencia_virtual.cnpj, agencia_virtual.telefone))
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br',2222213133,1520000000)
    print('Agência Virtual e seu site {}'.format(agencia_virtual.site))
    print('Agência Virtual e seu número:{}, \ncnpj: {} ,\nTelefone: {}'.format(agencia_virtual.numero, agencia_virtual.cnpj, agencia_virtual.telefone))


    #agencia_virtual.caixa = 15000
    print('Alterado o caixa para: {:,.2f}'.format(agencia_virtual.caixa))
    agencia_virtual.verificar_caixa()
    print('Lista de clientes ainda vazia do site virtual')
    print(agencia_virtual.clientes)

    print('Agência Premium')
    agencia_premium = AgenciaPremium(234255555, 152000000)

    print('Agência Premium e seu número:{}, \ncnpj: {} ,\nTelefone: {}'.format(agencia_premium.numero, agencia_premium.cnpj, agencia_premium.telefone))


    #agencia_premium.caixa = 100000
    #print('Alterado o caixa para: {:,.2f}'.format(agencia_premium.caixa))
    print('Premium e seu caixa para: {:,.2f}'.format(agencia_premium.caixa))
    agencia_premium.verificar_caixa()
    print()
    print('Dinheiro no caixa principal da agência R${:,.2f}'.format(agencia1.caixa))
    print('Dinheiro no caixa Virtual da agência R${:,.2f}'.format(agencia_virtual.caixa))

    print('Agencia Comum')
    agencia_comum = AgenciaComum(2222255555,2550000000)
    agencia_comum.verificar_caixa()
    print('Agencia Comum Tel: {} e CNPJ:{} '.format(agencia_comum.telefone,agencia_comum.cnpj ))
    print('Conta ou número da Agencia Comum {}'.format(agencia_comum.numero))


    print()
    print('Dados da agencia virtual, com o depositar do Paypal')
    print(' Depositar 20000 reais no Paypal, através da Agência Virtual')
    agencia_virtual.depositar_paypal(20000)
    print('Dinheiro no caixa geral agora : {:,.2f}'.format(agencia_virtual.caixa))
    print('Dinheiro no Paypal no momento : {:,.2f}'.format(agencia_virtual.caixa_paypal))

    agencia_premium.adicionar_cliente('Pedro Lirava', 1500000000, 10000)
    print(agencia_premium.clientes)

    agencia_premium.adicionar_cliente('Pedro Lirava', 1500000000, 50000000)
    print(agencia_premium.clientes)
    print('Agencia Premium para o {} e com o CPF:{}\nE seu patrimônio de R${:,.2f}'.format(agencia_premium.clientes[0][0],agencia_premium.clientes[0][1], agencia_premium.clientes[0][2]))

    #adicionar do cliente para a Agencia comum pega da classe geral
    agencia_comum.adicionar_cliente('New Name Bills', 12412431313, 10)
    print(agencia_comum.clientes)

    print('Agencia Comum para o {} e com o CPF:{}\nTem seu patrimônio de R${:,.2f}'.format(agencia_comum.clientes[0][0],agencia_comum.clientes[0][1], agencia_comum.clientes[0][2]))
    #print(agencia_comum.cpf)