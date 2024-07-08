#class sem precisar repetir , self seria o vendedor no exemplo
#pandas também é uma casse

class Vendedor():
      #atributos ou informacoes
      #pass
      #correto
      #toda a funcao que se cria, geramos o parametro self 
    def __init__(self,nome_vendedor):
         # se tivesse underline na frente, _meta_venda saberia que não é para alterar os dados
         self.nome = nome_vendedor
         self.sobrenome =''
         self.cpf =''
         self.vendas = 0
         self.meta_venda =500
         self.bonus = 0


    def vendeu(self, quantidade_vendas):
         self.vendas= quantidade_vendas
         self.calcular_bonus()

    #tudo dentro da mesma classe
    def calcular_bonus(self):
        if self.vendas > self.meta_venda:
           self.bonus =30
        else:
           self.bonus = 0
            