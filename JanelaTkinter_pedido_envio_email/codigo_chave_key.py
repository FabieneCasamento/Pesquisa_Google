#class sem precisar repetir , self seria a chave no exemplo
#pandas também é uma classe

class Chave_email():
      #atributos ou informacoes
      #pass
      #correto
      #toda a funcao que se cria, geramos o parametro self 
    def __init__(self):
         # se tivesse underline na frente, _meta_venda saberia que não é para alterar os dados
         minha_chave = 'CHAVE DO MEU E-MAIL'
         self.chavekey = minha_chave
         self.e_mail_meu ='MEUEMAIL@gmail.com'
         self.teste_envio = 'MEUEMAIL+teste@gmail.com'
